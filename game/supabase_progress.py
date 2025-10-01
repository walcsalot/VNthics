# Supabase Progress Tracking Integration for VNEthics
# Handles educational analytics and progress tracking

import json
from datetime import datetime
from supabase_config import supabase, create_progress_entry
from supabase_auth import supabase_auth

class SupabaseProgress:
    def __init__(self):
        self.local_progress = []
        
    def track_choice(self, scenario_id, choice_number, choice_text, choice_result, moral_impact):
        """Track a player's choice for analytics"""
        try:
            if not supabase_auth.is_authenticated():
                return self._local_track_choice(scenario_id, choice_number, choice_text, choice_result, moral_impact)
            
            if supabase.offline_mode:
                return self._offline_track_choice(scenario_id, choice_number, choice_text, choice_result, moral_impact)
            
            user_id = supabase_auth.get_current_user().get("id")
            
            progress_data = create_progress_entry(
                user_id, scenario_id, choice_number, choice_text, choice_result, moral_impact
            )
            
            response = supabase.make_request(
                "POST",
                "/game_progress",
                progress_data
            )
            
            if response.status_code in [200, 201]:
                return {
                    "success": True,
                    "message": "Progress tracked successfully"
                }
            else:
                # Fallback to local tracking
                return self._local_track_choice(scenario_id, choice_number, choice_text, choice_result, moral_impact)
                
        except Exception as e:
            print(f"Progress tracking error: {e}")
            return self._local_track_choice(scenario_id, choice_number, choice_text, choice_result, moral_impact)
    
    def track_scenario_start(self, scenario_id, scenario_name):
        """Track when a scenario is started"""
        return self.track_choice(scenario_id, 0, "scenario_start", scenario_name, 0)
    
    def track_scenario_end(self, scenario_id, ending_type, final_moral_score):
        """Track when a scenario is completed"""
        return self.track_choice(scenario_id, 999, "scenario_end", ending_type, final_moral_score)
    
    def get_user_progress(self, user_id=None):
        """Get progress data for a user"""
        try:
            if not user_id:
                if not supabase_auth.is_authenticated():
                    return self._local_get_progress()
                user_id = supabase_auth.get_current_user().get("id")
            
            if supabase.offline_mode:
                return self._offline_get_progress(user_id)
            
            response = supabase.make_request(
                "GET",
                f"/game_progress?user_id=eq.{user_id}&order=timestamp.desc"
            )
            
            if response.status_code == 200:
                progress_data = response.json()
                return {
                    "success": True,
                    "progress": progress_data
                }
            else:
                return self._local_get_progress()
                
        except Exception as e:
            print(f"Get progress error: {e}")
            return self._local_get_progress()
    
    def get_scenario_analytics(self, scenario_id):
        """Get analytics for a specific scenario"""
        try:
            if supabase.offline_mode:
                return self._offline_get_scenario_analytics(scenario_id)
            
            # Get all progress entries for this scenario
            response = supabase.make_request(
                "GET",
                f"/game_progress?scenario_id=eq.{scenario_id}&order=timestamp.desc"
            )
            
            if response.status_code == 200:
                progress_data = response.json()
                
                # Calculate analytics
                analytics = self._calculate_scenario_analytics(progress_data)
                
                return {
                    "success": True,
                    "analytics": analytics
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to get scenario analytics"
                }
                
        except Exception as e:
            print(f"Scenario analytics error: {e}")
            return {
                "success": False,
                "message": f"Analytics error: {str(e)}"
            }
    
    def get_moral_choice_stats(self, user_id=None):
        """Get statistics about moral choices made by user"""
        try:
            if not user_id:
                if not supabase_auth.is_authenticated():
                    return self._local_get_moral_stats()
                user_id = supabase_auth.get_current_user().get("id")
            
            if supabase.offline_mode:
                return self._offline_get_moral_stats(user_id)
            
            response = supabase.make_request(
                "GET",
                f"/game_progress?user_id=eq.{user_id}&moral_impact=not.is.null"
            )
            
            if response.status_code == 200:
                progress_data = response.json()
                stats = self._calculate_moral_stats(progress_data)
                
                return {
                    "success": True,
                    "stats": stats
                }
            else:
                return self._local_get_moral_stats()
                
        except Exception as e:
            print(f"Moral stats error: {e}")
            return self._local_get_moral_stats()
    
    def _calculate_scenario_analytics(self, progress_data):
        """Calculate analytics from progress data"""
        if not progress_data:
            return {
                "total_players": 0,
                "completion_rate": 0,
                "average_moral_score": 0,
                "choice_distribution": {},
                "common_choices": []
            }
        
        # Group by user
        user_progress = {}
        for entry in progress_data:
            user_id = entry["user_id"]
            if user_id not in user_progress:
                user_progress[user_id] = []
            user_progress[user_id].append(entry)
        
        total_players = len(user_progress)
        completed_players = 0
        total_moral_score = 0
        choice_counts = {}
        
        for user_id, entries in user_progress.items():
            # Check if user completed the scenario
            has_end = any(entry["choice_number"] == 999 for entry in entries)
            if has_end:
                completed_players += 1
            
            # Calculate moral score
            user_moral_score = sum(entry.get("moral_impact", 0) for entry in entries)
            total_moral_score += user_moral_score
            
            # Count choices
            for entry in entries:
                choice_text = entry.get("choice_text", "")
                if choice_text and choice_text not in ["scenario_start", "scenario_end"]:
                    choice_counts[choice_text] = choice_counts.get(choice_text, 0) + 1
        
        completion_rate = (completed_players / total_players * 100) if total_players > 0 else 0
        average_moral_score = (total_moral_score / total_players) if total_players > 0 else 0
        
        # Get most common choices
        common_choices = sorted(choice_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            "total_players": total_players,
            "completion_rate": round(completion_rate, 2),
            "average_moral_score": round(average_moral_score, 2),
            "choice_distribution": choice_counts,
            "common_choices": common_choices
        }
    
    def _calculate_moral_stats(self, progress_data):
        """Calculate moral choice statistics"""
        if not progress_data:
            return {
                "total_choices": 0,
                "positive_choices": 0,
                "negative_choices": 0,
                "neutral_choices": 0,
                "moral_balance": 0
            }
        
        total_choices = len(progress_data)
        positive_choices = sum(1 for entry in progress_data if entry.get("moral_impact", 0) > 0)
        negative_choices = sum(1 for entry in progress_data if entry.get("moral_impact", 0) < 0)
        neutral_choices = sum(1 for entry in progress_data if entry.get("moral_impact", 0) == 0)
        
        total_moral_impact = sum(entry.get("moral_impact", 0) for entry in progress_data)
        moral_balance = total_moral_impact / total_choices if total_choices > 0 else 0
        
        return {
            "total_choices": total_choices,
            "positive_choices": positive_choices,
            "negative_choices": negative_choices,
            "neutral_choices": neutral_choices,
            "moral_balance": round(moral_balance, 2),
            "positive_percentage": round((positive_choices / total_choices * 100), 2) if total_choices > 0 else 0,
            "negative_percentage": round((negative_choices / total_choices * 100), 2) if total_choices > 0 else 0
        }
    
    def _local_track_choice(self, scenario_id, choice_number, choice_text, choice_result, moral_impact):
        """Track choice locally"""
        entry = {
            "scenario_id": scenario_id,
            "choice_number": choice_number,
            "choice_text": choice_text,
            "choice_result": choice_result,
            "moral_impact": moral_impact,
            "timestamp": datetime.now().isoformat()
        }
        self.local_progress.append(entry)
        
        return {
            "success": True,
            "message": "Progress tracked locally"
        }
    
    def _local_get_progress(self):
        """Get local progress data"""
        return {
            "success": True,
            "progress": self.local_progress
        }
    
    def _local_get_moral_stats(self):
        """Get local moral statistics"""
        return self._calculate_moral_stats(self.local_progress)
    
    def _offline_track_choice(self, scenario_id, choice_number, choice_text, choice_result, moral_impact):
        """Track choice offline"""
        return self._local_track_choice(scenario_id, choice_number, choice_text, choice_result, moral_impact)
    
    def _offline_get_progress(self, user_id):
        """Get offline progress"""
        return self._local_get_progress()
    
    def _offline_get_moral_stats(self, user_id):
        """Get offline moral stats"""
        return self._local_get_moral_stats()
    
    def _offline_get_scenario_analytics(self, scenario_id):
        """Get offline scenario analytics"""
        scenario_progress = [entry for entry in self.local_progress if entry["scenario_id"] == scenario_id]
        analytics = self._calculate_scenario_analytics(scenario_progress)
        return {
            "success": True,
            "analytics": analytics
        }

# Global progress instance
supabase_progress = SupabaseProgress()
