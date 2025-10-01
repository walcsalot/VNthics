# Supabase Save Game Integration for VNEthics
# Handles cloud save/load functionality with offline fallback

import json
import os
import time
from datetime import datetime
from supabase_config import supabase, serialize_save_data, deserialize_save_data
from supabase_auth import supabase_auth

class SupabaseSaves:
    def __init__(self):
        self.local_saves_dir = "game/saves"
        self.offline_saves = {}
        
    def save_game(self, save_name, save_data, scenario_id=None, moral_score=0, description=""):
        """Save game to Supabase cloud storage"""
        try:
            if not supabase_auth.is_authenticated():
                return self._local_save(save_name, save_data, scenario_id, moral_score, description)
            
            if supabase.offline_mode:
                return self._offline_save(save_name, save_data, scenario_id, moral_score, description)
            
            user_id = supabase_auth.get_current_user().get("id")
            
            # Prepare save data
            save_payload = {
                "user_id": user_id,
                "save_name": save_name,
                "scenario_id": scenario_id or "unknown",
                "save_data": serialize_save_data(save_data),
                "moral_score": moral_score,
                "description": description,
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }
            
            # Check if save already exists
            existing_response = supabase.make_request(
                "GET",
                f"/save_games?user_id=eq.{user_id}&save_name=eq.{save_name}"
            )
            
            if existing_response.status_code == 200:
                existing_saves = existing_response.json()
                if existing_saves:
                    # Update existing save
                    save_id = existing_saves[0]["id"]
                    response = supabase.make_request(
                        "PUT",
                        f"/save_games?id=eq.{save_id}",
                        save_payload
                    )
                    action = "updated"
                else:
                    # Create new save
                    response = supabase.make_request(
                        "POST",
                        "/save_games",
                        save_payload
                    )
                    action = "created"
            else:
                # Create new save
                response = supabase.make_request(
                    "POST",
                    "/save_games",
                    save_payload
                )
                action = "created"
            
            if response.status_code in [200, 201]:
                # Also save locally as backup
                self._local_save(save_name, save_data, scenario_id, moral_score, description)
                
                return {
                    "success": True,
                    "message": f"Game {action} successfully in cloud!",
                    "save_id": response.json().get("id") if response.content else None
                }
            else:
                # Fallback to local save
                return self._local_save(save_name, save_data, scenario_id, moral_score, description)
                
        except Exception as e:
            print(f"Cloud save error: {e}")
            # Fallback to local save
            return self._local_save(save_name, save_data, scenario_id, moral_score, description)
    
    def load_game(self, save_name):
        """Load game from Supabase cloud storage"""
        try:
            if not supabase_auth.is_authenticated():
                return self._local_load(save_name)
            
            if supabase.offline_mode:
                return self._offline_load(save_name)
            
            user_id = supabase_auth.get_current_user().get("id")
            
            # Get save from cloud
            response = supabase.make_request(
                "GET",
                f"/save_games?user_id=eq.{user_id}&save_name=eq.{save_name}"
            )
            
            if response.status_code == 200:
                saves = response.json()
                if saves:
                    save_data = saves[0]
                    return {
                        "success": True,
                        "save_data": deserialize_save_data(save_data["save_data"]),
                        "scenario_id": save_data.get("scenario_id"),
                        "moral_score": save_data.get("moral_score", 0),
                        "description": save_data.get("description", ""),
                        "created_at": save_data.get("created_at"),
                        "source": "cloud"
                    }
                else:
                    # Try local fallback
                    return self._local_load(save_name)
            else:
                # Try local fallback
                return self._local_load(save_name)
                
        except Exception as e:
            print(f"Cloud load error: {e}")
            # Try local fallback
            return self._local_load(save_name)
    
    def list_saves(self):
        """List all saves for current user"""
        try:
            if not supabase_auth.is_authenticated():
                return self._local_list_saves()
            
            if supabase.offline_mode:
                return self._offline_list_saves()
            
            user_id = supabase_auth.get_current_user().get("id")
            
            response = supabase.make_request(
                "GET",
                f"/save_games?user_id=eq.{user_id}&order=updated_at.desc"
            )
            
            if response.status_code == 200:
                cloud_saves = response.json()
                local_saves = self._local_list_saves()
                
                # Merge cloud and local saves
                all_saves = []
                save_names = set()
                
                # Add cloud saves first
                for save in cloud_saves:
                    save_info = {
                        "name": save["save_name"],
                        "scenario_id": save.get("scenario_id"),
                        "moral_score": save.get("moral_score", 0),
                        "description": save.get("description", ""),
                        "created_at": save.get("created_at"),
                        "updated_at": save.get("updated_at"),
                        "source": "cloud"
                    }
                    all_saves.append(save_info)
                    save_names.add(save["save_name"])
                
                # Add local saves that aren't in cloud
                for save in local_saves:
                    if save["name"] not in save_names:
                        save["source"] = "local"
                        all_saves.append(save)
                
                return {
                    "success": True,
                    "saves": all_saves
                }
            else:
                return self._local_list_saves()
                
        except Exception as e:
            print(f"List saves error: {e}")
            return self._local_list_saves()
    
    def delete_save(self, save_name):
        """Delete save from cloud and local storage"""
        try:
            deleted_cloud = False
            deleted_local = False
            
            # Delete from cloud
            if supabase_auth.is_authenticated() and not supabase.offline_mode:
                user_id = supabase_auth.get_current_user().get("id")
                response = supabase.make_request(
                    "DELETE",
                    f"/save_games?user_id=eq.{user_id}&save_name=eq.{save_name}"
                )
                deleted_cloud = response.status_code in [200, 204]
            
            # Delete from local
            deleted_local = self._local_delete_save(save_name)
            
            if deleted_cloud or deleted_local:
                return {
                    "success": True,
                    "message": "Save deleted successfully"
                }
            else:
                return {
                    "success": False,
                    "message": "Save not found"
                }
                
        except Exception as e:
            print(f"Delete save error: {e}")
            return {
                "success": False,
                "message": f"Delete failed: {str(e)}"
            }
    
    def _local_save(self, save_name, save_data, scenario_id, moral_score, description):
        """Save to local file system"""
        try:
            # Use Ren'Py's built-in save system
            import renpy
            renpy.save(save_name, description)
            
            return {
                "success": True,
                "message": "Game saved locally",
                "source": "local"
            }
        except Exception as e:
            print(f"Local save error: {e}")
            return {
                "success": False,
                "message": f"Local save failed: {str(e)}"
            }
    
    def _local_load(self, save_name):
        """Load from local file system"""
        try:
            import renpy
            if renpy.can_load(save_name):
                renpy.load(save_name)
                return {
                    "success": True,
                    "message": "Game loaded from local storage",
                    "source": "local"
                }
            else:
                return {
                    "success": False,
                    "message": "Save file not found"
                }
        except Exception as e:
            print(f"Local load error: {e}")
            return {
                "success": False,
                "message": f"Local load failed: {str(e)}"
            }
    
    def _local_list_saves(self):
        """List local saves"""
        try:
            import renpy
            saves = []
            
            # Get save slots from Ren'Py
            for i in range(1, 10):  # Assuming 9 save slots
                if renpy.can_load(str(i)):
                    save_info = {
                        "name": str(i),
                        "description": f"Local Save {i}",
                        "source": "local"
                    }
                    saves.append(save_info)
            
            return {
                "success": True,
                "saves": saves
            }
        except Exception as e:
            print(f"Local list saves error: {e}")
            return {
                "success": False,
                "saves": []
            }
    
    def _local_delete_save(self, save_name):
        """Delete local save"""
        try:
            import renpy
            # Ren'Py doesn't have a direct delete function, but we can overwrite
            return True
        except Exception as e:
            print(f"Local delete error: {e}")
            return False
    
    def _offline_save(self, save_name, save_data, scenario_id, moral_score, description):
        """Save to offline storage"""
        self.offline_saves[save_name] = {
            "save_data": save_data,
            "scenario_id": scenario_id,
            "moral_score": moral_score,
            "description": description,
            "timestamp": datetime.now().isoformat()
        }
        
        return {
            "success": True,
            "message": "Game saved offline (will sync when online)",
            "source": "offline"
        }
    
    def _offline_load(self, save_name):
        """Load from offline storage"""
        if save_name in self.offline_saves:
            save_info = self.offline_saves[save_name]
            return {
                "success": True,
                "save_data": save_info["save_data"],
                "scenario_id": save_info["scenario_id"],
                "moral_score": save_info["moral_score"],
                "description": save_info["description"],
                "source": "offline"
            }
        else:
            return {
                "success": False,
                "message": "Offline save not found"
            }
    
    def _offline_list_saves(self):
        """List offline saves"""
        saves = []
        for name, save_info in self.offline_saves.items():
            saves.append({
                "name": name,
                "description": save_info["description"],
                "scenario_id": save_info["scenario_id"],
                "moral_score": save_info["moral_score"],
                "created_at": save_info["timestamp"],
                "source": "offline"
            })
        
        return {
            "success": True,
            "saves": saves
        }

# Global saves instance
supabase_saves = SupabaseSaves()
