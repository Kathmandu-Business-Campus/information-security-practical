def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []

    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared

def playfair_encrypt(plain_text, key):
    matrix = generate_playfair_matrix(key)
    prepared = prepare_text(plain_text)
    cipher = ''
    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher

def playfair_decrypt(cipher_text, key):
    matrix = generate_playfair_matrix(key)
    plain = ''
    for i in range(0, len(cipher_text), 2):
        a, b = cipher_text[i], cipher_text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            plain += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plain += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            plain += matrix[r1][c2] + matrix[r2][c1]
    return plain

# Demo
key = "KEYWORD"
plaintext = "HELLO WORLD"
encrypted = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(encrypted, key)

print("Playfair Cipher")
print(f"Key        : {key}")
print(f"Plaintext  : {plaintext}")
print(f"Encrypted  : {encrypted}")
print(f"Decrypted  : {decrypted}")
