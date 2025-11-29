# Attribute-Based Access Control Demo

print("=== Attribute-Based Access Control (ABAC) ===")

user_attr = {
    "alice": {"department": "IT", "level": 5},
    "bob": {"department": "HR", "level": 2}
}

resource_attr = {
    "file1": {"department": "IT", "min_level": 4},
    "file2": {"department": "HR", "min_level": 1}
}

def abac_access(user, resource):
    u_attr = user_attr.get(user)
    r_attr = resource_attr.get(resource)
    return u_attr["department"] == r_attr["department"] and u_attr["level"] >= r_attr["min_level"]

print("Bob access file1?", abac_access("bob","file1"))     # False
print("Alice access file1?", abac_access("alice","file1")) # True
