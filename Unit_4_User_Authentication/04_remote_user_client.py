import socket
import json
import getpass

HOST = '127.0.0.1'
PORT = 5000

def send_request(action, username, password):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        request = json.dumps({
            "action": action,
            "username": username,
            "password": password
        })
        s.sendall(request.encode())
        response = s.recv(1024).decode()
        print("🔐 Server Response:", response)

def main():
    while True:
        print("\nRemote User Authentication Client")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choice: ").strip()

        if choice == '3':
            break

        if choice not in ['1', '2']:
            print("Invalid choice.")
            continue

        username = input("Username: ").strip()
        password = getpass.getpass("Password: ")
        action = "register" if choice == '1' else "login"

        send_request(action, username, password)

if __name__ == "__main__":
    main()
