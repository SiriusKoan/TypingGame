from threading import Thread
import random
from ui import window, MultiWindow
from data import sentences
from client import Client

run = True
last_count = 0


def check():
    global run
    global last_count
    while run:
        sentence = window.text_label.cget("text").split()
        now = window.self_input.get().split()
        add = 0
        for word in now:
            if word in sentence:
                sentence.remove(word)
                add += 1
        window.word_count.set(str(last_count + add))
        if window.self_input_var.get() == window.text_label.cget("text"):
            sentence = random.choice(sentences)
            window.sentence.set(sentence)
            window.self_input_var.set("")
            last_count = int(window.word_count.get())


def end():
    global run
    run = False
    if isinstance(window, MultiWindow):
        client.end()
    window.destroy()


if __name__ == "__main__":
    if isinstance(window, MultiWindow):
        check_thread = Thread(target=check)
        check_thread.setDaemon(True)
        check_thread.start()
        client = Client(window)
        send_thread = Thread(target=client.send)
        send_thread.setDaemon(True)
        send_thread.start()
        receive_thread = Thread(target=client.receive)
        receive_thread.setDaemon(True)
        receive_thread.start()
    window.protocol("WM_DELETE_WINDOW", end)
    window.mainloop()
