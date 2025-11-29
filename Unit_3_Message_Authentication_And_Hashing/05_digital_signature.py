import rsa

(publicKey, privateKey) = rsa.newkeys(512)

message = b'My secure message'
signature = rsa.sign(message, privateKey, 'SHA-1')

# Verification
try:
    rsa.verify(message, signature + '00', publicKey)
    print("Signature verified!")
except:
    print("Invalid signature.")
