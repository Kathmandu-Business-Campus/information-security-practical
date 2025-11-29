"""
SSL/TLS Demo
Connects to a website using SSL/TLS and prints handshake details.
"""

import ssl
import socket

hostname = 'www.google.com'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(f"SSL established. Peer: {ssock.getpeercert()}")
        print(f"Cipher: {ssock.cipher()}")
        print(f"Protocol version: {ssock.version()}")
