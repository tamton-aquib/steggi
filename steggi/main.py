import cv2
import tkinter as tk
from . import converters, extractors
from tkinter import filedialog
from PIL import ImageTk, Image

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        menubar = tk.Menu(self)
        self.configure(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=False)
        filemenu.add_command(label='Save', command=self.write_img)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.destroy)

        extractmenu = tk.Menu(menubar, tearoff=False)
        extractmenu.add_command(label='planes', command=lambda: self.change_frame(self.converter))
        extractmenu.add_command(label='extract', command=lambda: self.change_frame(self.extractor))

        menubar.add_cascade(label='File', menu=filemenu)
        menubar.add_cascade(label='Extract', menu=extractmenu)

        self.frame = tk.Frame(self)
        self.frame.pack()

        tk.Button(self.frame, text="Upload image!", command=self.upload_image).pack()

    def write_img(self):
        filename = filedialog.asksaveasfilename(title="Save file")
        cv2.imwrite(filename, self.img)

    def upload_image(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Jpg files", "*.jpg"), ("Png files", "*.png")])
        self.img: cv2.numpy.ndarray = cv2.imread(self.filename)
        self.h, self.w, self.c = self.img.shape

        self.canvas = tk.Canvas(self.frame, width=self.w, height=self.h)
        # cv2.resize(self.img, dsize=(self.canvas.winfo_height(), self.canvas.winfo_width()))
        self.tk_img = ImageTk.PhotoImage(image=Image.fromarray(self.img))
        self.canvas.create_image(self.h/2, self.w/2, image=self.tk_img)
        self.canvas.pack()

        self.converter = converters.Converter(self)
        self.extractor = extractors.Extractor(self)

    def change_frame(self, elem):
        self.frame.forget()
        self.frame = elem.frame
        elem.refresh()
        self.frame.pack(**elem.packopts)
        # self.frame.update()

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
