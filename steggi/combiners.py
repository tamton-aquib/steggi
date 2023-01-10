import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

class Combiner:
    def __init__(self, root) -> None:
        self.root = root
        self.local_img = self.root.img
        self.h, self.w, _ = self.local_img.shape

        self.frame = tk.Frame(self.root)
        self.packopts = {"side": "left", "anchor": 'nw'}

        self.label = tk.Label(self.frame, text="noice")

        self.canvas = tk.Canvas(self.frame, width=self.w, height=self.h)
        self.canvas.pack()

        self.butt = tk.Button(self.frame, text="Combiner another", command=self.askopen)
        self.butt.pack()

        self.tk_img = ImageTk.PhotoImage(image=Image.fromarray(self.local_img))
        self.canvas.create_image(self.h/2, self.w/2, image=self.tk_img)

    def askopen(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Jpg files", "*.jpg"), ("Png files", "*.png")])
        self.newimg: cv2.numpy.ndarray = cv2.imread(self.filename)
        self.newimg = cv2.resize(self.newimg, (self.w, self.h))
        self.local_img = cv2.addWeighted(self.local_img, 0.5, self.newimg, 0.5, 0.0)
        self.refresh()

    def refresh(self):
        self.tk_img = ImageTk.PhotoImage(image=Image.fromarray(self.local_img))
        self.canvas.create_image(self.h/2, self.w/2, image=self.tk_img)
