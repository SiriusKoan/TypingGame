import tkinter as tk
import random
from data import sentences


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing")
        self.geometry("1000x500")
        self.text_label = tk.Label(self, text=random.choice(sentences))
        self.text_label.pack(fill="x")
        self.self_input = tk.Entry(self, width=100)
        self.self_input.pack()

