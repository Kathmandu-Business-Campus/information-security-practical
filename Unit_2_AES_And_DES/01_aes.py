from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES requires 16, 24, or 32 byte key
key = b'ThisIsASecretKey'  
data = input("Enter plaintext to encrypt: ").encode()

# Encrypt
cipher = AES.new(key, AES.MODE_CBC)  # CBC mode
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv = cipher.iv

print("Ciphertext (hex):", ct_bytes.hex())
print("IV (hex):", iv.hex())

# Decrypt
dec_cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(dec_cipher.decrypt(ct_bytes), AES.block_size)
print("Decrypted text:", pt.decode())
