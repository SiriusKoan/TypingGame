import tkinter as tk
import random
from data import sentences


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.sentence = tk.StringVar()
        self.sentence.set(random.choice(sentences))
        self.self_input_var = tk.StringVar()
        self.word_count = tk.StringVar()
        self.word_count.set("0")
        self.title("Typing")
        self.geometry("1000x500")

        self.text_label = tk.Label(self, textvariable=self.sentence)
        self.text_label.pack(fill="x")

        self.self_input = tk.Entry(self, width=100, textvariable=self.self_input_var)
        self.self_input.pack()

        self.count_label = tk.Label(self, textvariable=self.word_count)
        self.count_label.pack()
