import socket
import threading

#5011

HEADER = 64
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DIS_MESSAGE = "DiScOnNeCtEd!"
FORMAT = 'utf-8'

print(SERVER)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg: str): 
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b'' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send(" Hello world longer")
input()
send("Again")
input()
send("Again again")
input()
send("Again Again Again")
input()
send("Again Again Again Again Again")
input()
send(DIS_MESSAGE)