"""
PGP Email Encryption Demo
Demonstrates encrypting and decrypting a message using GPG library.
"""

"""
Download gpg from the url for windows:
https://gpg4win.org/download.html

No need to download for Mac and Linux
"""

from gnupg import GPG

gpg = GPG()  # Uses default home directory ~/.gnupg
message = "This is a confidential email message."

# Step 1: Generate key pair (students may skip if key exists)
input_data = gpg.gen_key_input(
    name_email="student@example.com",
    passphrase="testpass"
)
key = gpg.gen_key(input_data)

print("Generated key fingerprint:", key.fingerprint)

# Step 2: Encrypt the message
encrypted_data = gpg.encrypt(message, recipients=["student@example.com"])
print("\nEncrypted Message:\n", str(encrypted_data))

# Step 3: Decrypt the message
decrypted_data = gpg.decrypt(str(encrypted_data), passphrase="testpass")
print("\nDecrypted Message:\n", str(decrypted_data))
