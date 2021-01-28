import socket
import threading

#localhost
HOST='127.0.0.1'
PORT=9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        #ask user fo nickname
        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server \n".encode('utf-8'))
        client.send("Connected to the server".encode("utf-8"))

        thread= threading.Thread(target=handle,args=(client,))
        thread.start()

#handle function

def handle(client):
    while True:
        try:
            message=client.recv(1024)
            print(f"{nicknames[clients.index(client)]}: {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

print('server running')
receive()