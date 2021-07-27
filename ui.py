import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from time import sleep
from threading import Thread
import random
from data import sentences
from utils import multi_setup, single_setup, multi_down


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main")
        self.geometry("500x300")
        self.grid_columnconfigure(1, weight=100)
        self.room_id = tk.StringVar()
        self.single_btn = tk.Button(
            self, text="Single Player", command=self.open_single_window
        )
        self.single_btn.grid(column=0, row=2, padx=20)
        self.room_id_label = tk.Label(self, text="Room ID:")
        self.room_id_label.grid(column=1, row=0, padx=20)
        self.room_id_entry = tk.Entry(self, textvariable=self.room_id)
        self.room_id_entry.grid(column=1, row=1, padx=20)
        self.multi_btn = tk.Button(
            self, text="Multiple Players", command=self.open_multi_window
        )
        self.multi_btn.grid(column=1, row=2, padx=20)

    def open_single_window(self):
        game_window = SingleWindow(self)
        single_setup(game_window)

    def open_multi_window(self):
        if self.room_id.get():
            game_window = MultiWindow(self)
            multi_setup(game_window, self.room_id.get())
        else:
            messagebox.showerror("Error", "Unable to connect: No room ID is provided.")


class SingleWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Single Player")
        self.geometry("1000x500")
        self.font = tkFont.Font(family="Lucida Grande", size=18)
        self.sentence = tk.StringVar()
        self.sentence.set(random.choice(sentences))
        self.input_var = tk.StringVar()
        self.word_count = tk.IntVar()
        self.word_count.set(0)
        self.timer_var = tk.IntVar()
        self.timer_var.set(0)

        self.text_label = tk.Label(
            self,
            textvariable=self.sentence,
            font=self.font,
            anchor="w",
        )
        self.text_label.pack(fill="x")

        self.input = tk.Entry(self, textvariable=self.input_var, font=self.font)
        self.input.pack(fill="x")

        self.count_label = tk.Label(self, textvariable=self.word_count)
        self.count_label.pack()

        self.timer_label = tk.Label(self, text="Timer: ")
        self.timer_label.pack()
        self.timer = tk.Label(self, textvariable=self.timer_var)
        self.timer.pack()

        self.start_btn = tk.Button(self, text="Start", command=self.setup_timer)
        self.start_btn.pack()

    def setup_timer(self):
        self.word_count.set(0)
        self.input_var.set("")
        timer_thread = Thread(target=self.update_timer)
        timer_thread.setDaemon(True)
        timer_thread.start()

    def update_timer(self):
        time = 60
        self.timer_var.set(time)
        while True:
            if time == 0:
                self.input.config(state="disabled")
                exit()
            sleep(1)
            time -= 1
            self.timer_var.set(time)


class MultiWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Multiple Players")
        self.geometry("1300x600")
        self.protocol("WM_DELETE_WINDOW", lambda: multi_down(self))
        self.font = tkFont.Font(family="Lucida Grande", size=16)

        # yourself
        self.sentence = tk.StringVar()
        self.sentence.set(random.choice(sentences))
        self.input_var = tk.StringVar()
        self.word_count = tk.StringVar()
        self.word_count.set("0")

        self.text_label = tk.Label(
            self,
            textvariable=self.sentence,
            font=self.font,
            anchor="w",
        )
        self.text_label.grid(column=0, row=0)

        self.input = tk.Entry(
            self,
            textvariable=self.input_var,
            font=self.font,
            width=60,
        )
        self.input.grid(column=0, row=1)

        self.count_label = tk.Label(self, textvariable=self.word_count)
        self.count_label.grid(column=0, row=2)

        # other guy
        self.sentence_other = tk.StringVar()
        self.input_var_other = tk.StringVar()
        self.word_count_other = tk.StringVar()

        self.text_label_other = tk.Label(
            self, textvariable=self.sentence_other, font=self.font, anchor="w"
        )
        self.text_label_other.grid(column=1, row=0)

        self.input_other = tk.Entry(
            self,
            textvariable=self.input_var_other,
            state="disabled",
            font=self.font,
            width=60,
        )
        self.input_other.grid(column=1, row=1)

        self.count_label_other = tk.Label(self, textvariable=self.word_count_other)
        self.count_label_other.grid(column=1, row=2)


window = MainWindow()
