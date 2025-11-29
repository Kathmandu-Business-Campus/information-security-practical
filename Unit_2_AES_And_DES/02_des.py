from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES requires 8 byte key
key = b'8bytekey'  
data = input("Enter plaintext to encrypt: ").encode()

# Encrypt
cipher = DES.new(key, DES.MODE_CBC)  
ct_bytes = cipher.encrypt(pad(data, DES.block_size))
iv = cipher.iv

print("Ciphertext (hex):", ct_bytes.hex())
print("IV (hex):", iv.hex())

# Decrypt
dec_cipher = DES.new(key, DES.MODE_CBC, iv)
pt = unpad(dec_cipher.decrypt(ct_bytes), DES.block_size)
print("Decrypted text:", pt.decode())
