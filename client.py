import socket
from time import sleep
import json


class Client:
    def __init__(self, window) -> None:
        self.client = socket.socket()
        self.client.connect(("127.0.0.1", 8000))
        self.window = window

    def send(self):
        while True:
            input = self.window.self_input_var.get()
            sentence = self.window.sentence.get()
            count = self.window.word_count.get()
            json_string = json.dumps(
                {"input": input, "sentence": sentence, "count": count}
            )
            self.client.sendall(bytes(json_string, "utf-8"))
            # print("send: " + json_string)
            sleep(0.2)

    def receive(self):
        while True:
            data = self.client.recv(1024)
            if data:
                data = data.decode("utf-8")
                # print("receive: " + data[0 : data.index("}") + 1])
                try:
                    json_string = json.loads(data[: data.index("}") + 1])
                    self.window.sentence_other.set(json_string["sentence"])
                    self.window.other_input_var.set(json_string["input"])
                    self.window.word_count_other.set(json_string["count"])
                except Exception as e:
                    print(e)
            sleep(0.2)

    def end(self):
        self.client.close()
