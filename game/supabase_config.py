# Supabase Configuration for VNEthics
# This file handles all Supabase integration for user accounts and save games

import json
import requests
import hashlib
import time
from datetime import datetime
import os

class SupabaseConfig:
    def __init__(self):
        # Supabase project configuration
        # Replace these with your actual Supabase project details
        self.supabase_url = "https://qcgkynncqksshfjtkyrj.supabase.co"
        self.supabase_anon_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFjZ2t5bm5jcWtzc2hmanRreXJqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkyMzExNzYsImV4cCI6MjA3NDgwNzE3Nn0.neD0OaXV8CSZvFRhBMoXW3gS4shrhlNyH9SQ12l3RTc"
        self.supabase_service_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFjZ2t5bm5jcWtzc2hmanRreXJqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1OTIzMTE3NiwiZXhwIjoyMDc0ODA3MTc2fQ.cCaI7XtRDDLJYWIYXN1iwVqnOspMoJ8GuN3Q9cZ3DwE"  # For server-side operations
        
        # API endpoints
        self.auth_url = f"{self.supabase_url}/auth/v1"
        self.rest_url = f"{self.supabase_url}/rest/v1"
        self.storage_url = f"{self.supabase_url}/storage/v1"
        
        # Headers for API requests
        self.headers = {
            "apikey": self.supabase_anon_key,
            "Authorization": f"Bearer {self.supabase_anon_key}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }
        
        # Current user session
        self.current_user = None
        self.access_token = None
        self.refresh_token = None
        
        # Offline mode flag
        self.offline_mode = False
        
    def set_offline_mode(self, offline=True):
        """Enable/disable offline mode"""
        self.offline_mode = offline
        if offline:
            print("Supabase: Offline mode enabled")
        else:
            print("Supabase: Online mode enabled")
    
    def is_online(self):
        """Check if we can connect to Supabase"""
        if self.offline_mode:
            return False
        
        try:
            response = requests.get(f"{self.rest_url}/", headers=self.headers, timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def make_request(self, method, endpoint, data=None, use_auth=True):
        """Make HTTP request to Supabase with error handling"""
        if self.offline_mode:
            raise Exception("Offline mode - cannot make requests")
        
        url = f"{self.rest_url}{endpoint}"
        headers = self.headers.copy()
        
        if use_auth and self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, timeout=10)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data, timeout=10)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=headers, json=data, timeout=10)
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=headers, timeout=10)
            else:
                raise Exception(f"Unsupported HTTP method: {method}")
            
            if response.status_code >= 400:
                error_msg = f"Supabase API error: {response.status_code}"
                try:
                    error_data = response.json()
                    if "message" in error_data:
                        error_msg += f" - {error_data['message']}"
                except:
                    pass
                raise Exception(error_msg)
            
            return response
            
        except requests.exceptions.Timeout:
            raise Exception("Request timeout - check your internet connection")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection error - cannot reach Supabase")
        except Exception as e:
            raise Exception(f"Request failed: {str(e)}")

# Global Supabase instance
supabase = SupabaseConfig()

# Initialize Supabase connection
def init_supabase():
    """Initialize Supabase connection and check status"""
    try:
        if supabase.is_online():
            print("Supabase: Connected successfully")
            return True
        else:
            print("Supabase: Connection failed, enabling offline mode")
            supabase.set_offline_mode(True)
            return False
    except Exception as e:
        print(f"Supabase: Initialization error - {str(e)}")
        supabase.set_offline_mode(True)
        return False

# Utility functions for data serialization
def serialize_save_data(save_data):
    """Convert Ren'Py save data to JSON-serializable format"""
    try:
        # Convert any non-serializable objects to strings
        if isinstance(save_data, dict):
            serialized = {}
            for key, value in save_data.items():
                try:
                    json.dumps(value)  # Test if serializable
                    serialized[key] = value
                except:
                    serialized[key] = str(value)
            return serialized
        else:
            return str(save_data)
    except Exception as e:
        print(f"Error serializing save data: {e}")
        return {"error": str(e), "data": str(save_data)}

def deserialize_save_data(serialized_data):
    """Convert JSON data back to Ren'Py format"""
    try:
        return serialized_data
    except Exception as e:
        print(f"Error deserializing save data: {e}")
        return {}

# Progress tracking utilities
def create_progress_entry(user_id, scenario_id, choice_number, choice_text, choice_result, moral_impact):
    """Create a standardized progress entry"""
    return {
        "user_id": user_id,
        "scenario_id": scenario_id,
        "choice_number": choice_number,
        "choice_text": choice_text,
        "choice_result": choice_result,
        "moral_impact": moral_impact,
        "timestamp": datetime.now().isoformat()
    }
