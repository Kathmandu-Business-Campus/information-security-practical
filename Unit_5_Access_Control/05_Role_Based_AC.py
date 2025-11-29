# Role-Based Access Control Demo

print("=== Role-Based Access Control (RBAC) ===")
# Access is determined by user roles

roles = {
    "admin": ["read", "write", "delete"],
    "user": ["read"]
}

user_roles = {
    "alice": "admin",
    "bob": "user"
}

def can_access(user, action):
    role = user_roles.get(user)
    return action in roles.get(role, [])

print("Bob delete?", can_access("bob","delete"))      # False
print("Alice delete?", can_access("alice","delete"))  # True
