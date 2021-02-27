import socket
import threading

HEADER = 64
PORT = 5011
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DIS_MESSAGE = "DiScOnNeCtEd!"

print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"address: {addr} connected.")
    isConnected = True
    while isConnected:
        msg_length = conn.recv()

def start():
    server.listen()
    print(f"Listening on {SERVER} ...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn, addr))
        thread.start()
        print(f"Active Connection: {threading.active_count() -1}")
    
print("Server is running ..")
start()