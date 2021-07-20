# from threading import Thread
# import multiprocessing
from threading import Thread
from time import sleep
from ui import Window

window = Window()
run = True
def check():
    global run
    while run:
        if window.self_input.get() == "test":
            print("test")

def end():
    global run
    run = False
    window.destroy()

if __name__ == "__main__":
    thread = Thread(target=check)
    thread.start()
    window.protocol("WM_DELETE_WINDOW", end)
    window.mainloop()
