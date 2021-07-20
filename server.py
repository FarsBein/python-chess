import socket
import threading

HEADER = 64 # len of msg in bites 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATE = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected!")

    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMATE) # not going to pass until recives a message something like default await in Javascript
        msg_len = int(msg_len)
        msg = conn.recv(msg_len).decode(FORMATE)
        print(f"[{addr}]: \'{msg}\' ")
        
        if msg == DISCONNECT_MSG:
            connected = False
    conn.close()

def start():
    server.listen()
    print(f"[LISTINING] Server is listing on {SERVER}")
    while True:
        conn, addr = server.accept() # when knew connection is found store the values
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}") # (-1) for removing the start listening and capturing thread 
        
print('[STRARTING] server is starting...')
start()  
    