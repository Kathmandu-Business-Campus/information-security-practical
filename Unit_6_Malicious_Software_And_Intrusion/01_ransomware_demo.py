"""
Safe Ransomware Demonstration
Encrypts a file into a new file without deleting the original.
Educational only.
"""

from cryptography.fernet import Fernet

# Step 1: Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Step 2: Define file paths
input_file = "important_data.txt"
output_file = "important_data.encrypted"

# Step 3: Read original file
try:
    with open(input_file, "rb") as f:
        data = f.read()
except FileNotFoundError:
    print(f"Error: {input_file} not found! Please create this file first.")
    exit()

# Step 4: Encrypt the data
encrypted_data = cipher.encrypt(data)

# Step 5: Save encrypted file
with open(output_file, "wb") as f:
    f.write(encrypted_data)

# Step 6: Print outputs
print(f"{input_file} has been encrypted to {output_file}.")
print("NOTE: Actual ransomware would have deleted the original file, but we are NOT doing that for safety.")

# Step 7: Optional: Show key (for educational purposes)
print(f"Encryption key (for decryption demo): {key.decode()}")
