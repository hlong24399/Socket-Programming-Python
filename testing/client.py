import socket
import threading


HEADER = 64
PORT = 5060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DIS_MESSAGE = "DiScOnNeCtEd!"
FORMAT = 'utf-8'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print(f"This client: {SERVER}")

def send(msg: str): 
    print("Message sent.")    
    client.send(msg.encode(FORMAT))
    
send("Hello the server")

mess = input("Enter next message: ")
send(str(mess))

print("Sending the DiScOnNeCt....")
send(DIS_MESSAGE)
send("error message passed")


