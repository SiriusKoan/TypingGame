from threading import Thread
from time import sleep
import random
from ui import Window
from data import sentences

window = Window()
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
    window.destroy()


if __name__ == "__main__":
    thread = Thread(target=check)
    thread.setDaemon(True)
    thread.start()
    window.protocol("WM_DELETE_WINDOW", end)
    window.mainloop()
