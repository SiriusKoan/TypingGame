import socket
from time import sleep
import json


class Client:
    def __init__(self, window, room_id) -> None:
        self.client = socket.socket()
        self.connect()
        self.window = window
        self.room_id = room_id

    def connect(self):
        self.client.connect(("127.0.0.1", 8000))

    def send_room_id(self):
        self.client.sendall(bytes(json.dumps({"room_id": self.room_id}), "utf-8"))

    def send(self):
        while True:
            input = self.window.self_input_var.get()
            sentence = self.window.sentence.get()
            count = self.window.word_count.get()
            json_string = json.dumps(
                {
                    "room_id": self.room_id,
                    "input": input,
                    "sentence": sentence,
                    "count": count,
                }
            )
            try:
                self.client.sendall(bytes(json_string, "utf-8"))
            except ConnectionResetError:
                self.connect()
            # print("send: " + json_string)
            sleep(0.3)

    def receive(self):
        self.window.sentence_other.set("No connection now.")
        while True:
            data = self.client.recv(1024).decode("utf-8")
            if data != "down":
                data = data[: data.index("}") + 1]
                # print("receive: " + data[0 : data.index("}") + 1])
                try:
                    json_string = json.loads(data)
                    self.window.sentence_other.set(json_string["sentence"])
                    self.window.other_input_var.set(json_string["input"])
                    self.window.word_count_other.set(json_string["count"])
                except Exception as e:
                    print(e)
            else:
                self.window.sentence_other.set("No connection now.")
            sleep(0.3)

    def end(self):
        self.client.close()
