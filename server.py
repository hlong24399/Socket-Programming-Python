import socket
import threading

#5011

FORMAT = 'utf-8'
HEADER = 64
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DIS_MESSAGE = "DiScOnNeCtEd!"

# print(socket.gethostname())
print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.settimeout(10)

def handle_client(conn, addr):

    print(f"address: {addr} connected.")
    is_connected=True

    while is_connected:
        # print(f"{conn.recv(HEADER).decode(FORMAT)}")
        # msg_length, msg = conn.recv(HEADER).decode(FORMAT)
        # msg = conn.recv(HEADER).decode(FORMAT)
        # print(f"{msg_length} --- {msg}")
        # if msg_length:
        #     msg_length = int(msg_length)
        #     if msg == DIS_MESSAGE:
        #         isConnected = False
        conn.send("Msg received".encode(FORMAT))
    conn.close()

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