from tkinter import *
from PIL import Image, ImageTk

on_press_ratio = 0.086
on_release_ratio = 0.08

class FunctionButton(Canvas):
    def __init__(self, parent, command, img_path=None):
        Canvas.__init__(self, parent.window, borderwidth=0,
                           relief="flat", highlightthickness=0, bg='white')
        self.command = command
        self.parent = parent
        self.width = on_press_ratio * parent.width
        self.height = on_press_ratio * parent.width
        self.img_path = img_path
        self.img = ImageTk.PhotoImage(Image.open("image/"+self.img_path).resize((int(on_release_ratio*self.parent.width),
                                                                                int(on_release_ratio*self.parent.width))))

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
        self.img = ImageTk.PhotoImage(Image.open("image/"+self.img_path).resize((int(on_release_ratio * self.parent.width),
                                                                                int(on_release_ratio * self.parent.width))))
        self.draw()
        if self.command is not None:
            self.command()
