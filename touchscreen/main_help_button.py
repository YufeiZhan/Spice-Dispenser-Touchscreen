from tkinter import *
from PIL import Image, ImageTk


class HelpButton(Canvas):
    def __init__(self, parent, msg):
        Canvas.__init__(self, parent.window, borderwidth=0,
                           relief="flat", highlightthickness=0, bg='white')
        self.command = None
        self.parent = parent
        self.width = 0.05 * parent.width
        self.height = 0.05 * parent.width
        self.msg = msg
        self.img = ImageTk.PhotoImage(Image.open("image/reset_button.png").resize((int(0.05*self.parent.width), int(0.05*self.parent.width))))

        self.configure(width=self.width, height=self.height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.draw()

    def draw(self):
        self.create_image(self.width/2, self.height/2, image=self.img)

    def _on_press(self, event):
        self.delete('all')
        self.img = ImageTk.PhotoImage(Image.open(self.img_path).resize((int(self.width), int(self.height))))
        self.draw()


    def _on_release(self, event=None):
        self.delete('all')
        self.img = ImageTk.PhotoImage(Image.open(self.img_path).resize((int(0.08 * self.parent.width), int(0.08 * self.parent.width))))
        self.draw()
        if self.command is not None:
            self.command()
