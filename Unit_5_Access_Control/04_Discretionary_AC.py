# Discretionary Access Control Demo

print("=== Discretionary Access Control (DAC) ===")
# Owner of object decides who can access it

dac_matrix = {
    "alice": {"file1": "rw", "file2": "r"},  # Alice owns these files
    "bob": {"file1": "r", "file2": ""}
}

def check_dac(user, file, mode):
    rights = dac_matrix.get(user, {}).get(file, "")
    return mode in rights

print("Bob write file1?", check_dac("bob", "file1", "w"))    # False
print("Alice write file1?", check_dac("alice", "file1", "w")) # True
