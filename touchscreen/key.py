from tkinter import *
from PIL import Image, ImageTk


class Key(Canvas):
    def __init__(self, keyboard, name):
        Canvas.__init__(self, keyboard.window, borderwidth=0,
                           relief="flat", highlightthickness=0, bg='white')
        self.command = keyboard.parent.compartments[keyboard.parent.selected.get()].update_spice_name(name)
        self.keyboard = keyboard
        self.width = 0.086 * keyboard.width
        self.height = 0.086 * keyboard.width
        #self.img_path = img_path
        #self.img = ImageTk.PhotoImage(Image.open("image/"+self.img_path).resize((int(0.08*self.parent.width), int(0.08*self.parent.width))))

        self.configure(width=self.width, height=self.height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.draw()

    def draw(self):
        self.create_image(self.width/2, self.height/2, image=self.img)

    def _on_press(self, event):
        self.delete('all')
        self.img = ImageTk.PhotoImage(Image.open("image/"+self.img_path).resize((int(self.width), int(self.height))))
        self.draw()

    def _on_release(self, event=None):
        self.delete('all')
        self.img = ImageTk.PhotoImage(Image.open("image/"+self.img_path).resize((int(0.08 * self.parent.width), int(0.08 * self.parent.width))))
        self.draw()
        if self.command is not None:
            self.command()
