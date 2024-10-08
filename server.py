import threading
import socket

host = '::1' 
port = 59000
server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except BrokenPipeError:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break

def receive():
    while True:
        print('Server is running and listening')
        client, address = server.accept()
        print(f'Connection is established with {str(address)}')
        try:
            client.send('alias?'.encode('utf-8'))
            alias = client.recv(1024).decode('utf-8')
            aliases.append(alias)
            clients.append(client)
            print(f'The alias of this client is {alias}')
            broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
            client.send('You are now connected!'.encode('utf-8'))
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()
        except BrokenPipeError:
            client.close()

if __name__ == "__main__":
    receive()
