import hashlib
import os
import getpass
import base64

# Simulated database (in-memory dictionary)
user_db = {
    "plain": {},
    "digest": {},
    "derived": {}
}


# 1. Plain text password storage (insecure)
def register_plain(username, password):
    user_db["plain"][username] = password


def authenticate_plain(username, password):
    stored = user_db["plain"].get(username)
    return stored == password


# 2. Message Digest using SHA256 (no salt)
def register_digest(username, password):
    hash_obj = hashlib.sha256(password.encode())
    user_db["digest"][username] = hash_obj.hexdigest()


def authenticate_digest(username, password):
    stored = user_db["digest"].get(username)
    hash_obj = hashlib.sha256(password.encode())
    return stored == hash_obj.hexdigest()


# 3. Derived password using PBKDF2 (secure)
def register_derived(username, password):
    salt = os.urandom(16)
    derived_key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    user_db["derived"][username] = {
        "salt": salt,
        "hash": derived_key
    }


def authenticate_derived(username, password):
    stored = user_db["derived"].get(username)
    if not stored:
        return False
    salt = stored["salt"]
    derived_key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return stored["hash"] == derived_key


# 4. Show raw stored credentials
def show_credentials():
    print("\n--- Stored Credentials ---")

    # Plain Text
    print("\n[Plain Text]")
    for user, pwd in user_db["plain"].items():
        print(f"{user}: {pwd}")

    # SHA256 Digest
    print("\n[SHA256 Digest]")
    for user, hash_val in user_db["digest"].items():
        print(f"{user}: {hash_val}")

    # Derived Passwords (PBKDF2)
    print("\n[PBKDF2 Derived]")
    for user, data in user_db["derived"].items():
        salt_b64 = base64.b64encode(data['salt']).decode()
        hash_b64 = base64.b64encode(data['hash']).decode()
        print(f"{user}:")
        print(f"  Salt (base64): {salt_b64}")
        print(f"  Hash (base64): {hash_b64}")

    print("\n---------------------------")


# Main Interface
def main():
    print("Password Authentication Demo")
    print("----------------------------")
    while True:
        print("\nChoose Option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("4. Show Raw Credentials")
        choice = input("Choice: ").strip()

        if choice == '4':
            show_credentials()
            continue
        elif choice == '3':
            break
        elif choice not in ('1', '2'):
            print("Invalid choice.")
            continue

        method = input("Method (plain/digest/derived): ").strip().lower()
        if method not in user_db:
            print("Invalid method.")
            continue

        username = input("Username: ").strip()
        password = getpass.getpass("Password: ")

        if choice == '1':
            if method == 'plain':
                register_plain(username, password)
            elif method == 'digest':
                register_digest(username, password)
            elif method == 'derived':
                register_derived(username, password)
            print("✅ User registered successfully.")

        elif choice == '2':
            if method == 'plain':
                result = authenticate_plain(username, password)
            elif method == 'digest':
                result = authenticate_digest(username, password)
            elif method == 'derived':
                result = authenticate_derived(username, password)

            if result:
                print("✅ Authentication successful!")
            else:
                print("❌ Authentication failed!")


if __name__ == "__main__":
    main()
