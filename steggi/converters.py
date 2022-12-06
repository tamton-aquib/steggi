import tkinter as tk
from PIL import ImageTk, Image
import cv2

class Converter:
    def __init__(self, root) -> None:
        self.root = root
        self.h, self.w, _ = self.root.img.shape

        self.planes_set_label_canvas_buttons_binds()
        self.packopts = {}

        self.idx = 0
        self.img_list = [
            {'name': "normal", "data": self.root.img},
            {'name': "xor", "data": 255 - self.root.img},
            {"name": "greyscale", "data": cv2.cvtColor(self.root.img, cv2.COLOR_BGR2GRAY)},
            {"name": "hsv", "data": cv2.cvtColor(self.root.img, cv2.COLOR_BGR2HSV)},
            # {"name": "laplacian", "data": cv2.Laplacian(self.root.img, cv2.CV_64F)},
            {"name": "lab", "data": cv2.cvtColor(self.root.img, cv2.COLOR_BGR2LAB)},
            {"name": "gaussian", "data": cv2.GaussianBlur(self.root.img, (7, 7), 0)},
            {"name": "edges", "data": cv2.Canny(self.root.img, 100, 200)}, # NOTE: edge detection
            {"name": "dst", "data": cv2.fastNlMeansDenoisingColored(self.root.img, None, 10, 10, 7, 15)}, # NOTE: looks nice
            {"name": "bitwise_not", "data": cv2.bitwise_not(self.root.img)},
        ]

    def planes_set_label_canvas_buttons_binds(self):
        self.frame = tk.Frame(self.root)

        self.label = tk.Label(self.frame, text='Normal')
        self.label.pack()

        self.canvas = tk.Canvas(self.frame, width=self.w, height=self.h)
        self.canvas.pack()

        tk.Button(self.frame, text='prev', command=self.sub_idx).pack()
        tk.Button(self.frame, text='next', command=self.add_idx).pack()

    def add_idx(self):
        if self.idx < len(self.img_list)-1:
            self.idx += 1
            self.refresh()

    def sub_idx(self):
        if self.idx > 0:
            self.idx -= 1
            self.refresh()

    def refresh(self):
        img = self.img_list[self.idx]
        self.tk_img = ImageTk.PhotoImage(image=Image.fromarray(img['data']))
        self.canvas.create_image(self.h/2, self.w/2, image=self.tk_img)
        self.label.configure(text=img['name'].capitalize())
