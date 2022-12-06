import tkinter as tk

class Extractor:
    def __init__(self, root, img) -> None:
        self.img = img
        self.root = root
        self.h, self.w, _ = self.img.shape

        self.planes_set_label_canvas_buttons_binds()

    def planes_set_label_canvas_buttons_binds(self):
        self.frame = tk.Frame(self.root)

        self.label = tk.Label(self.frame, text='Hallllo from Extractor!')
        self.label.pack()
