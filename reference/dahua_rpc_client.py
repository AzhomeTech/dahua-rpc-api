import requests
import hashlib
import json

# --- CONFIGURATION ---
CAMERA_IP = "http://192.168.1.108" # Change this to your camera's IP
USERNAME = "admin"
PASSWORD = "YourPasswordHere"      # Change this to your password

# The Dahua endpoints we found in rpcBase.js
LOGIN_URL = f"{CAMERA_IP}/RPC2_Login"
RPC_URL = f"{CAMERA_IP}/RPC2"

# A helper function to replicate Dahua's password hashing
def generate_dahua_hash(user, password, realm, random_str):
    # Step 1: MD5(user:realm:password)
    hash1_str = f"{user}:{realm}:{password}"
    hash1 = hashlib.md5(hash1_str.encode('utf-8')).hexdigest()

    # Step 2: MD5(user:random:hash1)
    hash2_str = f"{user}:{random_str}:{hash1}"
    hash2 = hashlib.md5(hash2_str.encode('utf-8')).hexdigest()

    return hash2

def main():
    session = requests.Session()
    request_id = 1

    print("Step 1: Sending First Login request...")
    # Send empty password to get the realm and random token
    payload1 = {
        "method": "global.login",
        "params": {
            "userName": USERNAME,
            "password": "",
            "clientType": "Web3.0"
        },
        "id": request_id
    }

    response1 = session.post(LOGIN_URL, json=payload1).json()
    request_id += 1

    # Extract the security tokens from the error response
    if "error" in response1 or response1.get("result") == False:
        params = response1.get("params", {})
        realm = params.get("realm")
        random_str = params.get("random")
        session_id = response1.get("session")

        print(f"-> Received Realm: {realm}")
        print(f"-> Received Random Token: {random_str}")
    else:
        print("Failed to get login challenge.")
        return

    print("\nStep 2: Calculating Hash and Sending Second Login request...")
    hashed_password = generate_dahua_hash(USERNAME, PASSWORD, realm, random_str)

    payload2 = {
        "method": "global.login",
        "params": {
            "userName": USERNAME,
            "password": hashed_password,
            "clientType": "Web3.0"
        },
        "id": request_id,
        "session": session_id
    }

    response2 = session.post(LOGIN_URL, json=payload2).json()
    request_id += 1

    if response2.get("result"):
        # The session ID is updated after a successful login
        session_id = response2.get("session")
        print(f"-> SUCCESS! Logged in. Session ID: {session_id}")
    else:
        print("-> Login Failed! Check your password.")
        return

    # --- NOW WE CAN SEND ANY COMMAND WE WANT ---
    print("\nStep 3: Sending the 'Holy Grail' command to list all features...")

    holy_grail_payload = {
        "method": "system.listMethod",
        "params": None,
        "id": request_id,
        "session": session_id
    }

    final_response = session.post(RPC_URL, json=holy_grail_payload).json()

    methods = final_response.get("params", {}).get("method", [])
    print(f"\nAwesome! Your camera supports {len(methods)} different commands.")
    print("Here is a sample of the first 20 commands:")
    for method in methods[:20]:
        print(f" - {method}")

if __name__ == "__main__":
    main()
