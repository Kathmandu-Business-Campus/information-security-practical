import hashlib
import os

# Paths to your MD5 collision files
files = ["md5_collision_demo_files/hello", "md5_collision_demo_files/erase"]

# Check if files exist
for f in files:
    if not os.path.exists(f):
        raise FileNotFoundError(f"{f} not found!")

# Function to compute hash
def file_hash(path, algo="md5"):
    h = hashlib.new(algo)
    with open(path, "rb") as file:
        h.update(file.read())
    return h.hexdigest()

# Display hashes of files
print("=== MD5 Collision Demonstration ===")
for f in files:
    print(f"\n=== {f} ===")
    print("MD5:     ", file_hash(f, "md5"))
    print("SHA1:    ", file_hash(f, "sha1"))
    print("SHA256:  ", file_hash(f, "sha256"))

# Compare files byte by byte
print("\nContent difference (first 64 bytes shown where different):")
with open(files[0], "rb") as f1, open(files[1], "rb") as f2:
    b1 = f1.read()
    b2 = f2.read()

if b1 == b2:
    print("Files are identical (should not happen with collision demo).")
else:
    for i, (byte1, byte2) in enumerate(zip(b1, b2)):
        if byte1 != byte2:
            print(f"Byte {i}: hello={hex(byte1)} erase={hex(byte2)}")
            if i > 64:
                print("... (truncated)")
                break

# --------------------------
# SHA-256 Collision Resistance Demo
# --------------------------
print("\n=== SHA-256 Collision Resistance Demonstration ===")
strings = ["hello", "hello!"]

for s in strings:
    hash_val = hashlib.sha256(s.encode()).hexdigest()
    print(f"SHA-256('{s}') = {hash_val}")
