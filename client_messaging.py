import socket

client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

def send_message(alias, message):
    client_socket.send(f'{alias}: {message}'.encode('utf-8'))
