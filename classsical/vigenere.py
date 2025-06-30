def vigenere_encrypt(plain_text, keyword):
    result = ''
    keyword = keyword.upper()
    i = 0
    for char in plain_text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            k = ord(keyword[i % len(keyword)]) - 65
            result += chr((ord(char.upper()) - 65 + k) % 26 + 65)
            i += 1
        else:
            result += char
    return result

def vigenere_decrypt(cipher_text, keyword):
    result = ''
    keyword = keyword.upper()
    i = 0
    for char in cipher_text:
        if char.isalpha():
            shift = 65
            k = ord(keyword[i % len(keyword)]) - 65
            result += chr((ord(char) - shift - k + 26) % 26 + shift)
            i += 1
        else:
            result += char
    return result

# Example
text = "HELLO WORLD"
keyword = "KEY"
encrypted = vigenere_encrypt(text, keyword)
decrypted = vigenere_decrypt(encrypted, keyword)

print(f"Vigenère Encrypted: {encrypted}")
print(f"Vigenère Decrypted: {decrypted}")
