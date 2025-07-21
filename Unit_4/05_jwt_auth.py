import jwt
import datetime
import time

# Secret key to sign the JWT
SECRET_KEY = "my_super_secret_key_456"

# Dummy user database
users = {
    "alice": "password123",
    "bob": "letmein"
}

# Generate a JWT token
def generate_token(username):
    payload = {
        "user": username,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)  # 30 sec expiry
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Validate and decode the JWT token
def verify_token(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}

# Main logic
def main():
    print("=== JWT Authentication Demo ===")
    username = input("Username: ")
    password = input("Password: ")

    if users.get(username) == password:
        print("[✔] Login successful")
        token = generate_token(username)
        print("\nGenerated JWT Token:")
        print(token)

        print("\nSimulating access to protected resource...")
        time.sleep(2)
        decoded = verify_token(token)
        if "error" in decoded:
            print("[✘] Access denied:", decoded["error"])
        else:
            print("[✔] Access granted. Hello,", decoded["user"])
    else:
        print("[✘] Invalid username or password")

if __name__ == "__main__":
    main()
