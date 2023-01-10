import tkinter as tk
from PIL import Image
from PIL.ExifTags import TAGS
import os

class Extractor:
    def __init__(self, root) -> None:
        self.root = root
        self.h, self.w, _ = self.root.img.shape

        self.frame = tk.Frame(self.root, bg='#ff0000')
        self.packopts = {"side": "left", "anchor": 'nw'}

        exifdata = Image.fromarray(self.root.img, 'RGB').getexif()
        # exifdata = Image.open(self.root.filename).getexif()

        self.result  = f"{'Filename: ':25} {os.path.basename(self.root.filename)}\n"
        self.result += f"{'Directory: ':25} {os.path.dirname(self.root.filename)}"

        for tagid in exifdata:
            tagname = TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)
            self.result += f"{tagname:25}: {value}\n"

        self.label = tk.Label(self.frame, text=self.result)
        self.label.pack()

    def refresh(self):
        pass
