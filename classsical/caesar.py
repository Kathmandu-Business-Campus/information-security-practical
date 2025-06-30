def caesar_encrypt(plain_text, key):
    result = ''
    for char in plain_text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(cipher_text, key):
    return caesar_encrypt(cipher_text, -key)

# Example
text = "HELLO WORLD"
key = 3
encrypted = caesar_encrypt(text, key)
decrypted = caesar_decrypt(encrypted, key)

print(f"Caesar Encrypted: {encrypted}")
print(f"Caesar Decrypted: {decrypted}")
