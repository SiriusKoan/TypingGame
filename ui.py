import tkinter as tk
import tkinter.font as tkFont
import random
from data import sentences


class SingleWindow(tk.Tk):
    def __init__(self):
        super().__init__()
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


class MultiWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.font = tkFont.Font(family="Lucida Grande", size=16)
        self.title("Typing")
        self.geometry("1300x600")

        # self
        self.sentence = tk.StringVar()
        self.sentence.set(random.choice(sentences))
        self.self_input_var = tk.StringVar()
        self.word_count = tk.StringVar()
        self.word_count.set("0")

        self.text_label = tk.Label(self, textvariable=self.sentence, font=self.font)
        self.text_label.grid(column=0, row=0)

        self.self_input = tk.Entry(
            self, textvariable=self.self_input_var, font=self.font, width=60
        )
        self.self_input.grid(column=0, row=1)

        self.count_label = tk.Label(self, textvariable=self.word_count)
        self.count_label.grid(column=0, row=2)

        # other guy
        self.sentence_other = tk.StringVar()
        self.sentence_other.set(random.choice(sentences))
        self.other_input_var = tk.StringVar()
        self.word_count_other = tk.StringVar()
        self.word_count_other.set("0")

        self.text_label_other = tk.Label(
            self, textvariable=self.sentence_other, font=self.font
        )
        self.text_label_other.grid(column=1, row=0)

        self.other_input = tk.Entry(
            self, textvariable=self.other_input_var, font=self.font, width=60
        )
        self.other_input.grid(column=1, row=1)

        self.count_label_other = tk.Label(self, textvariable=self.word_count_other)
        self.count_label_other.grid(column=1, row=2)


window = MultiWindow()
