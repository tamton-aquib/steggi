import cv2
import tkinter as tk
from steggi import converters
from tkinter import filedialog
from PIL import ImageTk, Image

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting menubar
        menubar = tk.Menu(self)
        self.configure(menu=menubar)

        filemenu = tk.Menu(menubar)
        filemenu.add_command(label='Quit', command=self.destroy)

        extractmenu = tk.Menu(menubar)
        extractmenu.add_command(label='planes', command=self.change_frame)

        menubar.add_cascade(label='File', menu=filemenu)
        menubar.add_cascade(label='Extract', menu=extractmenu)

        self.frame = tk.Frame(self, bg="#11121d")
        self.frame.pack()

        tk.Button(self.frame, text="Upload image!", command=self.upload_image).pack()


    def upload_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Jpg files", "*.jpg"), ("Png files", "*.png")])
        self.img: cv2.numpy.ndarray = cv2.imread(filename)
        # self.img = cv2.resize(self.img, dsize=(self.frame.winfo_height(), self.frame.winfo_width()))
        self.h, self.w, _ = self.img.shape

        self.tk_img = ImageTk.PhotoImage(image=Image.fromarray(self.img))
        canvas = tk.Canvas(self.frame, width=self.w, height=self.h)
        canvas.create_image(self.h/2, self.w/2, image=self.tk_img)
        canvas.pack()

        self.converter = converters.Converter(self, self.img)

    def change_frame(self):
        self.frame.forget()
        self.frame = self.converter.frame
        self.frame.pack()
        # self.frame.update()
        self.converter.refresh()

app = App()
app.mainloop()
