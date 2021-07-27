import random
from threading import Thread
from time import sleep
from data import sentences
from client import Client

# setup
client = None


def check(window):
    # global last_count
    last_count = 0
    try:
        while True:
            sentence = window.text_label.cget("text").split()
            now = window.input.get().split()
            add = 0
            for word in now:
                if word in sentence:
                    sentence.remove(word)
                    add += 1
            window.word_count.set(last_count + add)
            if window.input_var.get() == window.text_label.cget("text"):
                sentence = random.choice(sentences)
                window.sentence.set(sentence)
                window.input_var.set("")
                last_count = window.word_count.get()
    except:
        exit()


def single_setup(game_window):
    check_thread = Thread(target=check, args=(game_window,))
    check_thread.setDaemon(True)
    check_thread.start()


def multi_setup(game_window, room_id):
    global client
    check_thread = Thread(target=check, args=(game_window,))
    check_thread.setDaemon(True)
    check_thread.start()
    client = Client(game_window, room_id)
    client.send_room_id()
    sleep(0.2)  # wait for server receiving room id
    send_thread = Thread(target=client.send)
    send_thread.setDaemon(True)
    send_thread.start()
    receive_thread = Thread(target=client.receive)
    receive_thread.setDaemon(True)
    receive_thread.start()


def multi_down(window):
    global client
    try:
        client.end()
    except:
        pass
    window.destroy()
