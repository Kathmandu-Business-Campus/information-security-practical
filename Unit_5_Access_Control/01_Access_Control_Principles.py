# Access Control Principles Demo
# Demonstrates fundamental concepts: least privilege, separation of duties

print("=== Access Control Principles ===")
print("1. Least Privilege: Users only get access needed for their tasks.")
print("2. Separation of Duties: Prevents fraud by splitting responsibilities.")
print("3. Confidentiality, Integrity, Availability (CIA) principle.")
print("\nExample:")
users = {"alice": "admin", "bob": "user"}

def principle_demo(user):
    if user == "admin":
        print(f"{user}: Can perform all tasks.")
    else:
        print(f"{user}: Limited access only.")

principle_demo("alice")
principle_demo("bob")
