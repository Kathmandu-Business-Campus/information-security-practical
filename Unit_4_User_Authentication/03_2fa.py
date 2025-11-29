import pyotp
import hashlib
import os
import getpass
import qrcode
import base64

# In-memory database
user_db = {}  # username -> {salt, hash, totp_secret}


def register(username, password):
    # Generate password hash
    salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)

    # Generate TOTP secret for Google Authenticator
    totp_secret = pyotp.random_base32()

    user_db[username] = {
        'salt': salt,
        'hash': pwd_hash,
        'totp_secret': totp_secret
    }

    # Display QR Code for Google Authenticator
    totp_uri = pyotp.totp.TOTP(totp_secret).provisioning_uri(name=username, issuer_name="SecureApp2FA")
    qr = qrcode.make(totp_uri)
    print("📷 Scan this QR code with Google Authenticator:")
    qr.show()
    print(f"🔐 Or manually enter this secret: {totp_secret}")
    print("✅ Registration complete.")


def verify_password(username, password):
    user = user_db.get(username)
    if not user:
        return False
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), user['salt'], 100_000)
    return pwd_hash == user['hash']


def verify_totp(username, otp_code):
    user = user_db.get(username)
    if not user:
        return False
    totp = pyotp.TOTP(user['totp_secret'])
    return totp.verify(otp_code)


def main():
    while True:
        print("\n🔐 Two-Factor Auth with Google Authenticator")
        print("1. Register")
        print("2. Login with 2FA")
        print("3. Exit")
        choice = input("Choice: ").strip()

        if choice == '1':
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ")
            register(username, password)

        elif choice == '2':
            username = input("Username: ").strip()
            password = getpass.getpass("Password: ")

            if not verify_password(username, password):
                print("❌ Invalid username or password.")
                continue

            otp = input("Enter 6-digit OTP from Google Authenticator: ").strip()
            if verify_totp(username, otp):
                print(f"✅ Login successful. Welcome, {username}!")
            else:
                print("❌ Invalid OTP.")

        elif choice == '3':
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
