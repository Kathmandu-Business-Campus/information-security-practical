import socket
import threading
import hashlib
import os
import json
import datetime
import sys

HOST = '127.0.0.1'
PORT = 5000
user_db = {}
LOG_FILE = "auth.log"


def log_event(addr, username, action, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] {addr[0]} - {action.upper()} - {username} - {status}"
    print(log_msg)
    with open(LOG_FILE, "a") as f:
        f.write(log_msg + "\n")


def hash_password(password, salt=None):
    if not salt:
        salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)
    return salt, pwd_hash


def handle_client(conn, addr):
    print(f"🔗 Connected by {addr}")
    try:
        data = conn.recv(1024).decode()
        request = json.loads(data)

        action = request.get("action")
        username = request.get("username")
        password = request.get("password")

        if not all([action, username, password]):
            conn.sendall("❌ Missing fields.".encode())
            return

        if action == "register":
            if username in user_db:
                conn.sendall("❌ User already exists.".encode())
                log_event(addr, username, "register", "failure (exists)")
                return
            salt, pwd_hash = hash_password(password)
            user_db[username] = {"salt": salt.hex(), "hash": pwd_hash.hex()}
            conn.sendall("✅ Registered successfully.".encode())
            log_event(addr, username, "register", "success")

        elif action == "login":
            user = user_db.get(username)
            if not user:
                conn.sendall("❌ User not found.".encode())
                log_event(addr, username, "login", "failure (not found)")
                return
            salt = bytes.fromhex(user["salt"])
            pwd_hash = bytes.fromhex(user["hash"])
            _, entered_hash = hash_password(password, salt)

            if entered_hash == pwd_hash:
                conn.sendall(f"✅ Login successful. Welcome, {username}!".encode())
                log_event(addr, username, "login", "success")
            else:
                conn.sendall("❌ Invalid password.".encode())
                log_event(addr, username, "login", "failure (wrong password)")

        else:
            conn.sendall("❌ Invalid action.".encode())
            log_event(addr, username, action, "failure (invalid action)")
    except Exception as e:
        conn.sendall(f"❌ Error: {e}".encode())
        log_event(addr, "unknown", "error", str(e))
    finally:
        conn.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"🛡️ Server listening on {HOST}:{PORT} (Press Ctrl+C to stop)")

        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

    except KeyboardInterrupt:
        print("\n🛑 Keyboard interrupt received. Shutting down server...")
    except Exception as e:
        print(f"❌ Server error: {e}")
    finally:
        server_socket.close()
        print("🔌 Port closed. Server exited cleanly.")
        sys.exit(0)


if __name__ == "__main__":
    start_server()
