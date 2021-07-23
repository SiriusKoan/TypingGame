import tkinter as tk
import tkinter.font as tkFont
import random
from data import sentences
from utils import multi_setup, single_setup


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.single_btn = tk.Button(
            self, text="Single Player", command=self.open_single_window
        )
        self.single_btn.pack()

        self.multi_btn = tk.Button(
            self, text="Multiple Players", command=self.open_multi_window
        )
        self.multi_btn.pack()

    def open_single_window(self):
        game_window = SingleWindow(self)
        single_setup(game_window)

    def open_multi_window(self):
        game_window = MultiWindow(self)
        multi_setup(game_window)


class SingleWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.font = tkFont.Font(family="Lucida Grande", size=18)
        self.sentence = tk.StringVar()
        self.sentence.set(random.choice(sentences))
        self.self_input_var = tk.StringVar()
        self.word_count = tk.StringVar()
        self.word_count.set("0")
        self.title("Typing")
        self.geometry("1000x500")

        self.text_label = tk.Label(self, textvariable=self.sentence, font=self.font)
        self.text_label.pack(fill="x")

        self.self_input = tk.Entry(
            self, textvariable=self.self_input_var, font=self.font
        )
        self.self_input.pack(fill="x")

        self.count_label = tk.Label(self, textvariable=self.word_count)
        self.count_label.pack()


class MultiWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.font = tkFont.Font(family="Lucida Grande", size=16)
        self.title("Typing")
        self.geometry("1300x600")

        # yourself
        self.sentence = tk.StringVar()
        self.sentence.set(random.choice(sentences))
        self.self_input_var = tk.StringVar()
        self.word_count = tk.StringVar()
        self.word_count.set("0")

        self.text_label = tk.Label(self, textvariable=self.sentence, font=self.font)
        self.text_label.grid(column=0, row=0)

        self.self_input = tk.Entry(
            self,
            textvariable=self.self_input_var,
            font=self.font,
            width=60,
        )
        self.self_input.grid(column=0, row=1)

        self.count_label = tk.Label(self, textvariable=self.word_count)
        self.count_label.grid(column=0, row=2)

        # other guy
        self.sentence_other = tk.StringVar()
        self.other_input_var = tk.StringVar()
        self.word_count_other = tk.StringVar()

        self.text_label_other = tk.Label(
            self,
            textvariable=self.sentence_other,
            font=self.font,
        )
        self.text_label_other.grid(column=1, row=0)

        self.other_input = tk.Entry(
            self,
            textvariable=self.other_input_var,
            state="disabled",
            font=self.font,
            width=60,
        )
        self.other_input.grid(column=1, row=1)

        self.count_label_other = tk.Label(self, textvariable=self.word_count_other)
        self.count_label_other.grid(column=1, row=2)


window = MainWindow()
