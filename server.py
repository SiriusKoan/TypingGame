import socket
import threading
import json
from threading import Thread


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 8000))
server.listen(10)
clients = []
rooms = dict()


def shutdown_process(current_client):
    current_client.close()
    for room in rooms:
        if current_client in rooms[room]:
            room_id = room
            for client in rooms[room_id]:
                if client != current_client:
                    client.sendall(bytes("down", "utf-8"))
            break


def receive(current_client):
    while True:
        try:
            data = json.loads(current_client.recv(1024).decode("utf-8"))
            room_id = data.pop("room_id")
            # print("receive: " + data[0 : data.index("}") + 1])
            for client in rooms[room_id]:
                if client != current_client:
                    # print("send: " + data)
                    try:
                        client.sendall(bytes(json.dumps(data), "utf-8"))
                    except:
                        rooms[room_id].remove(client)
        except Exception as e:
            shutdown_process(current_client)
            clients.remove(current_client)
            print(f"{current_client}: Connection close because of {e}.")
            exit()


while True:
    print(threading.active_count())
    current_client, _ = server.accept()
    print(f"{current_client}: Connected.")
    data = json.loads(current_client.recv(1024).decode("utf-8"))
    room_id = data.get("room_id", None)
    if not room_id:
        shutdown_process(current_client)
        print("Disconnect because client does not send room id.")
    else:
        if current_client not in clients:
            clients.append(current_client)
            if not rooms.get(room_id, None):
                rooms[room_id] = []
            rooms[room_id].append(current_client)
        receive_thread = Thread(target=receive, args=(current_client,))
        receive_thread.setDaemon(True)
        receive_thread.start()
