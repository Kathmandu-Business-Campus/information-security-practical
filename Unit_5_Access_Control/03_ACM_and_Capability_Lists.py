# Access Control Matrix (ACM) and Capability Lists Demo

print("=== Access Control Matrix ===")
# ACM: Table mapping subjects to objects and their rights
ac_matrix = {
    "alice": {"file1": "rw", "file2": "r"},
    "bob": {"file1": "r", "file2": ""}
}

for user, objects in ac_matrix.items():
    print(f"{user}: {objects}")

print("\n=== Capability Lists ===")
# Capability List: Per-subject list of accessible objects and rights
capability_list = ac_matrix  # In this simple demo, same as ACM
for user, caps in capability_list.items():
    print(f"{user} capabilities: {caps}")
