import socket
from threading import Thread

HEADER = 64 # len of msg in bites 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATE = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMATE) # translate to bites
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMATE) # translate to bites 
    send_len += b' ' * (HEADER - len(send_len)) # b' ' bit representation of ' '
    client.send(send_len)
    client.send(message)
    
def write():
    x = input()
    if x == 'q':
        return 'done'
    else:
        send(x)
        return None

def receive():
    print(client.recv(2048).decode(FORMATE))

while True:
    s = Thread(target = write)
    r = Thread(target = receive)
    
    s.start()
    r.start()
    

    
