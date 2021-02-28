import socket
import threading

#5011

FORMAT = 'utf-8'
HEADER = 64
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
DIS_MESSAGE = "DiScOnNeCtEd!"

print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.settimeout(10)

def handle_client(conn : socket.socket , addr : socket.AddressInfo):

    print(f"address: {addr} connected.")
    is_connected=True

    while is_connected:
        msg_recv = conn.recv(64)
        if msg_recv:
            print(f"from client {addr}: \"{msg_recv.decode(FORMAT)}\"")
            if msg_recv.decode(FORMAT) == DIS_MESSAGE:
                is_connected = False
            # conn.send(b"Got a message from Client")
    print("Conn closes")    
    conn.close()
    

def start():
    server.listen()
    print(f"Listening on {SERVER} ...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn, addr))
        print("in thread")
        thread.start()
        print(f"Active Connection: {threading.active_count() -1}")
    
print("Server is running ..")
start()
 