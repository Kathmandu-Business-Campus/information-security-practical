import os
import hashlib
import secrets
import getpass
import base64
import time

# Simulated database
user_db = {}       # Stores username and password hash
token_store = {}   # Stores token -> username and expiry

TOKEN_EXPIRY_SECONDS = 60 * 5  # Tokens valid for 5 minutes

# Register a new user
def register(username, password):
    salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    user_db[username] = {
        'salt': salt,
        'hash': pwd_hash
    }
    print("✅ User registered.")

# Login with username/password and get token
def login(username, password):
    user = user_db.get(username)
    if not user:
        print("❌ User not found.")
        return

    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), user['salt'], 100_000)
    if pwd_hash == user['hash']:
        token = secrets.token_urlsafe(32)
        token_store[token] = {
            'username': username,
            'expiry': time.time() + TOKEN_EXPIRY_SECONDS
        }
        print(f"✅ Login successful! Your token:\n{token}")
    else:
        print("❌ Incorrect password.")

# Authenticate using token
def authenticate_with_token(token):
    data = token_store.get(token)
    if not data:
        print("❌ Invalid token.")
        return

    if time.time() > data['expiry']:
        print("⚠️ Token has expired.")
        del token_store[token]
        return

    print(f"✅ Token valid. Authenticated as: {data['username']}")

# Display all stored data (for demo)
def show_raw():
    print("\n--- Users ---")
    for u, v in user_db.items():
        print(f"{u}:")
        print(f"  Salt: {base64.b64encode(v['salt']).decode()}")
        print(f"  Hash: {base64.b64encode(v['hash']).decode()}")
    print("\n--- Active Tokens ---")
    for t, v in token_store.items():
        print(f"{t[:8]}... -> {v['username']} (expires in {int(v['expiry'] - time.time())}s)")
    print("-------------------")

# Main CLI loop
def main():
    while True:
        print("\nToken Authentication Demo")
        print("1. Register")
        print("2. Login (Get Token)")
        print("3. Authenticate With Token")
        print("4. Show Raw Data")
        print("5. Exit")

        choice = input("Choose: ").strip()
        if choice == '1':
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ")
            register(username, password)
        elif choice == '2':
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ")
            login(username, password)
        elif choice == '3':
            token = input("Enter Token: ").strip()
            authenticate_with_token(token)
        elif choice == '4':
            show_raw()
        elif choice == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
