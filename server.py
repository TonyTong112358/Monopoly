import socket

import _thread

import sys

PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "127.0.0.1"
HEADERSIZE = 10
hash = "utf-8"
msg = "Welcome to the server"
print(f"{len(msg):<10} {msg}, you are hosting on {SERVER}")








with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((SERVER,PORT))
    except socket.error as e:
        print(e)
    s.listen(10)
    clientsocket, address = s.accept()
    
    print(f"Connected succesffuly to {address}")

    while True:
        data = clientsocket.recv(1024)
        print(data)
        # clientsocket.send(bytes("welcome to the server",hash))
        # clientsocket.close()
            


