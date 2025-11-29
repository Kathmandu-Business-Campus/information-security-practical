# Subjects, Objects and Access Rights Demo

print("=== Subjects, Objects, and Access Rights ===")
# Subject = active entity (user/process)
# Object = resource (file, record)
# Access rights = read/write/execute

subjects = ["alice", "bob"]
objects = ["file1", "file2"]

access_rights = {
    "alice": {"file1": "rw", "file2": "r"},
    "bob": {"file1": "r", "file2": ""}
}

for s in subjects:
    for o in objects:
        rights = access_rights[s][o]
        print(f"Subject {s} has rights '{rights}' on Object {o}")
