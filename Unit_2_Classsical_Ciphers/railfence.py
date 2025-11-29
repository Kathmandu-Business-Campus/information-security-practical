def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(''.join(row) for row in fence)

def rail_fence_decrypt(cipher_text, rails):
    pattern = [[] for _ in range(len(cipher_text))]
    rail = 0
    direction = 1
    for i in range(len(cipher_text)):
        pattern[i] = rail
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    counts = [pattern.count(r) for r in range(rails)]
    rail_chars = []
    i = 0
    for count in counts:
        rail_chars.append(list(cipher_text[i:i+count]))
        i += count

    result = ''
    for r in pattern:
        result += rail_chars[r].pop(0)
    return result

# Example
text = "HELLO WORLD"
rails = 3
encrypted = rail_fence_encrypt(text, rails)
decrypted = rail_fence_decrypt(encrypted, rails)

print(f"Rail Fence Encrypted: {encrypted}")
print(f"Rail Fence Decrypted: {decrypted}")
