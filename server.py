import socket
import threading
from threading import Thread


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8000))
server.listen(10)
clients = []


def receive(current_client):
    while True:
        try:
            data = current_client.recv(1024).decode("utf-8")
            # print("receive: " + data[0 : data.index("}") + 1])
            for client in clients:
                if client != current_client:
                    # print("send: " + data)
                    client.sendall(bytes(data, "utf-8"))
        except Exception as e:
            current_client.shutdown(2)
            current_client.close()
            clients.remove(current_client)
            for client in clients:
                if client != current_client:
                    client.sendall(bytes("down", "utf-8"))
            print(f"{current_client}: Connection close because {e}.")
            exit()


while True:
    print(threading.active_count())
    current_client, _ = server.accept()
    print(f"{current_client}: Connected.")
    if current_client not in clients:
        clients.append(current_client)
    receive_thread = Thread(target=receive, args=(current_client,))
    receive_thread.setDaemon(True)
    receive_thread.start()
