import threading 
import socket 

alias = input('Choose an alias >>>>')
client = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
client.connect(('127.0.0.1',59000))

def client_recieve():
    while True:
        try:
            message=client.recv(1024).decode('utf-8d')
            if message =="alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message) 
        except:
            print('Error!')
            client.close()
            break

def client_send():
    while True:
        message = f'{alias}: {input("")}'
        clinet.send(message.encode('utf-8')) 

recieve_thread = threading.Thread(target=client_recieve)
recieve_thread.start()

send_thread=threading.Thread(target=client_send)
send_thread.start()