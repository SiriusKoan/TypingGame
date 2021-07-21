import socket
from threading import Thread
from time import sleep


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8000))
server.listen(10)
clients = []


def accept():
    current_client, _ = server.accept()
    print(current_client)
    if current_client not in clients:
        clients.append(current_client)
    receive_thread = Thread(target=receive, args=(current_client,))
    receive_thread.setDaemon(True)
    receive_thread.start()


def receive(current_client):
    while True:
        data = current_client.recv(1024).decode("utf-8")
        print("receive: " + data[0 : data.index("}") + 1])
        for client in clients:
            if client != current_client:
                send_thread = Thread(
                    target=send, args=(client, data[0 : data.index("}") + 1])
                )
                send_thread.setDaemon(True)
                send_thread.start()


def send(client, data):
    while True:
        print("send: " + data)
        client.sendall(bytes(data, "utf-8"))
        sleep(0.5)


while True:
    accept_thread = Thread(target=accept)
    accept_thread.setDaemon(True)
    accept_thread.start()
