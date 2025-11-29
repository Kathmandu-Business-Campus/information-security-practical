from Crypto.Hash import MD4
import hashlib

msg = b'Hello World'
print("MD5:", hashlib.md5(msg).hexdigest())

# MD4 using PyCryptodome
md4 = MD4.new()
md4.update(msg)
print("MD4:", md4.hexdigest())
