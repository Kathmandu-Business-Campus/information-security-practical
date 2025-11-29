from hashlib import sha256

def authenticate(msg, key):
    return sha256((msg + key).encode()).hexdigest()

msg = "Hello students"
key = "secret123"

auth_tag = authenticate(msg, key)
print("Authentication tag:", auth_tag)

# Now simulate tampering
tampered = "Hello studentz"
print("Tampered Auth:", authenticate(tampered, key))
