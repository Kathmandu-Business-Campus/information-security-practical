# Identity, Credential, and Access Management Demo

print("=== Identity and Credential Management ===")

credentials = {
    "alice": "password123",
    "bob": "qwerty"
}

def login(user, pwd):
    return credentials.get(user) == pwd

print("Alice login correct?", login("alice","password123")) # True
print("Bob login wrong?", login("bob","1234"))              # False
