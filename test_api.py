import requests
import json
import uuid

# Generate a unique email
unique_id = str(uuid.uuid4())[:8]
email = f"test_{unique_id}@example.com"
password = "password123"

# 1. Register
reg_url = "http://127.0.0.1:8000/auth/register"
reg_data = {
    "username": f"user_{unique_id}",
    "email": email,
    "password": password
}
headers = {"Content-Type": "application/json"}

print(f"--- Registering {email} ---")
reg_response = requests.post(reg_url, json=reg_data, headers=headers)
print(f"Status Code: {reg_response.status_code}")
print(f"Response: {reg_response.text}")

# 2. Login
if reg_response.status_code == 201:
    print(f"\n--- Logging in {email} ---")
    login_url = "http://127.0.0.1:8000/auth/login"
    # Note: OAuth2PasswordRequestForm uses form data, not JSON
    login_data = {
        "username": email,
        "password": password
    }
    login_response = requests.post(login_url, data=login_data)
    print(f"Status Code: {login_response.status_code}")
    print(f"Response: {login_response.text}")
    
    if login_response.status_code == 200:
        token = login_response.json().get("access_token")
        
        # 3. Get /users/me
        print("\n--- Fetching /users/me ---")
        me_url = "http://127.0.0.1:8000/users/me"
        me_headers = {"Authorization": f"Bearer {token}"}
        me_response = requests.get(me_url, headers=me_headers)
        print(f"Status Code: {me_headers}") # Debug headers
        print(f"Status Code: {me_response.status_code}")
        print(f"Response: {me_response.text}")

