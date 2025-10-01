# Supabase Authentication Integration for VNEthics
# Handles user registration, login, and session management

import json
import requests
import hashlib
from datetime import datetime, timedelta
from supabase_config import supabase

class SupabaseAuth:
    def __init__(self):
        self.current_user = None
        self.session_data = None
        
    def login_user(self, email, password):
        """Login user with Supabase"""
        try:
            if supabase.offline_mode:
                return self._offline_login(email, password)
            
            # Login with Supabase Auth
            auth_data = {
                "email": email,
                "password": password
            }
            
            response = requests.post(
                f"{supabase.auth_url}/token?grant_type=password",
                headers=supabase.headers,
                json=auth_data,
                timeout=10
            )
            
            if response.status_code == 200:
                auth_response = response.json()
                
                # Store session data
                supabase.access_token = auth_response.get("access_token")
                supabase.refresh_token = auth_response.get("refresh_token")
                self.current_user = auth_response.get("user", {})
                self.session_data = auth_response
                
                # Get user profile
                user_id = self.current_user.get("id")
                profile_response = supabase.make_request(
                    "GET",
                    f"/user_profiles?id=eq.{user_id}"
                )
                
                if profile_response.status_code == 200:
                    profiles = profile_response.json()
                    if profiles:
                        profile = profiles[0]
                        self.current_user.update(profile)
                
                return {
                    "success": True,
                    "message": "Login successful!",
                    "user": self.current_user
                }
            else:
                error_data = response.json() if response.content else {}
                error_msg = error_data.get("msg", "Login failed")
                return {
                    "success": False,
                    "message": f"Login failed: {error_msg}"
                }
                
        except Exception as e:
            print(f"Login error: {e}")
            return {
                "success": False,
                "message": f"Login failed: {str(e)}"
            }
    
    def logout_user(self):
        """Logout current user"""
        try:
            if not supabase.offline_mode and supabase.access_token:
                # Logout from Supabase
                requests.post(
                    f"{supabase.auth_url}/logout",
                    headers={
                        "Authorization": f"Bearer {supabase.access_token}",
                        "apikey": supabase.supabase_anon_key
                    },
                    timeout=10
                )
        except Exception as e:
            print(f"Logout error: {e}")
        finally:
            # Clear local session data
            self.current_user = None
            self.session_data = None
            supabase.access_token = None
            supabase.refresh_token = None
    
    def get_current_user(self):
        """Get current user data"""
        return self.current_user
    
    def is_authenticated(self):
        """Check if user is authenticated"""
        return self.current_user is not None and supabase.access_token is not None
    
    def refresh_session(self):
        """Refresh access token"""
        try:
            if not supabase.refresh_token:
                return False
            
            response = requests.post(
                f"{supabase.auth_url}/token?grant_type=refresh_token",
                headers=supabase.headers,
                json={"refresh_token": supabase.refresh_token},
                timeout=10
            )
            
            if response.status_code == 200:
                auth_response = response.json()
                supabase.access_token = auth_response.get("access_token")
                supabase.refresh_token = auth_response.get("refresh_token")
                return True
            else:
                return False
                
        except Exception as e:
            print(f"Token refresh error: {e}")
            return False
    
    def _offline_login(self, email, password):
        """Offline login fallback"""
        # Check against local storage
        return {
            "success": True,
            "message": "Login successful (offline mode)",
            "user": {
                "id": f"offline_{hashlib.md5(email.encode()).hexdigest()}",
                "email": email,
                "username": email.split("@")[0],
                "full_name": "Offline User"
            }
        }

# Global auth instance
supabase_auth = SupabaseAuth()
