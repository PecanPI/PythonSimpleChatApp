import socket
import threading

#localhost
HOST='127.0.0.1'
PORT='9090'

server = socket.socket(socket.AF_INET, scoket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients=[]
nicknames=[]

#broadcast function
def broadcast(message):
    for client in clients:
        client.send(message)

#receive function

def receive():
    while True:
        client, address = server.accept()
        print(f"Connecected with {str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname=client.receive(1024)

        nicknames.append(nickname)
        clients.append(client)

        print("Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server\n".encode(utf-8))
        client.send("Connected to the server".encode("utf-8"))


#handle function