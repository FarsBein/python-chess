import socket
import threading

HEADER = 64 # len of msg in bites 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATE = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(2)


def broadcast(message, exception = None):
    for client in clients:
        if not exception or exception != client:
            client.send(message)

def client_left(client):
    clients.remove(client)
    client.close()
    broadcast(f'A client has left the chat room!, total: {len(clients)}'.encode('utf-8'))

# Function to receive clients' connections
def handle_client(client, address):
    while True:
        try:
            message = client.recv(1024)
            if message.decode() == 'quit' or message.decode() == 'q': 
                client.send('quit'.encode('utf-8'))
                break
            print(f'{str(address)}: ', message.decode())
            broadcast(message, client)
        except:
            break
    client_left(client)
    
# Main function to receive the clients connection
def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        
        print(f'connection is established with {str(address)}')
        
        clients.append(client)
        
        broadcast(f'New client has connected, total: {len(clients)}'.encode('utf-8'), client)
        client.send('you are now connected!'.encode('utf-8'))
        
        
        thread = threading.Thread(target=handle_client, args=(client,address))
        thread.start()

receive()