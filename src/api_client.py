import requests
import os
from error_handler import handle_api_error

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:5000")

def login(email, password):
    """Authenticate user and return a token."""
    try:
        response = requests.post(f"{API_BASE_URL}/login", json={"email": email, "password": password})
        
        # Check if status code is OK (200) and the response contains a token
        if response.status_code == 200:
            # Check if the response body contains the token
            response_data = response.json()
            token = response_data.get("token")
            
            if token:
                return token  # Return token if it's found
            else:
                print("❌ Invalid credentials. No token received.")
                return None  # Explicitly return None if no token is provided
        else:
            print("❌ Authentication failed. Please check your credentials and try again.")
            return None  # Return None if status code is not 200 (authentication failed)
    
    except requests.RequestException as e:
        return handle_api_error(e)

def get_auth_headers(token):
    """Return headers with authentication token."""
    return {"Authorization": f"Bearer {token}"}

def get_cars(token, page=1, limit=10):
    """Fetch paginated car data with authentication."""
    try:
        headers = get_auth_headers(token)
        response = requests.get(f"{API_BASE_URL}/cars?page={page}&limit={limit}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return handle_api_error(e)
