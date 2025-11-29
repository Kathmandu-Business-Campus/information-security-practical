import hashlib

print("SHA1:", hashlib.sha1(b"hello").hexdigest())
print("SHA256:", hashlib.sha256(b"hello").hexdigest())
