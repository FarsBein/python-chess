import socket
import threading

HEADER = 64 # len of msg in bites 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATE = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "quit" or message == "q":
                break
            else:
                print(f"received: {message}")
        except:
            print('Error in client_receive!')
            break
    client.close()


def client_send():
    while True:
        try:
            message = input("")
            client.send(message.encode('utf-8'))
            if message == "quit" or message == "q":
                    break
        except:
            print('Error in client_send!')
            break
    client.close()


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()