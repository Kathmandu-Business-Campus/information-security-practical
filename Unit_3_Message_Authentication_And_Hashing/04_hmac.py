import hmac
import hashlib

key = b'secret'
msg = b'authenticated message'

tag = hmac.new(key, msg, hashlib.sha256).hexdigest()
print("HMAC:", tag)
