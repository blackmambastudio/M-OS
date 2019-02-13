import socket
import sys

sock = None
def open():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 6060)
    sock.connect(server_address)

def write(message):
    if not sock:
        print("socket not open")
        return
    # Send data
    sock.send(message)

def close():
    sock.close()