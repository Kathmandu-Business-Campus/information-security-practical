import hashlib
import os
import difflib

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

# Compare files line by line (read as text if possible)
print("\n=== Content Difference (line-by-line) ===")
try:
    with open(files[0], "r", encoding="utf-8", errors="ignore") as f1, open(files[1], "r", encoding="utf-8", errors="ignore") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    diff = difflib.unified_diff(lines1, lines2, fromfile='hello', tofile='erase', lineterm='')
    diff_output = list(diff)
    if diff_output:
        for line in diff_output:
            print(line)
    else:
        print("No visible line differences found (files may be binary).")

except Exception as e:
    print("Could not read files as text. Showing byte-level differences instead.\n")
    # Fallback: byte-level differences
    with open(files[0], "rb") as f1, open(files[1], "rb") as f2:
        b1 = f1.read()
        b2 = f2.read()
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
