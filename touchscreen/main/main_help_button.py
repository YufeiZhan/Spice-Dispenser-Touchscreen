from tkinter import *
from PIL import Image, ImageTk
from main.main_help_message import HelpMessage


class HelpButton(Canvas):
    def __init__(self, parent, command=None):
        Canvas.__init__(self, parent.window, borderwidth=0,
                        relief="flat", highlightthickness=0, bg='white')
        self.parent = parent
        self.width = 0.03 * parent.width
        self.height = 0.03 * parent.width
        self.command = command
        self.img = ImageTk.PhotoImage(
            Image.open("./image/QuestionM.png").resize((int(0.9 * self.width), int(0.9 * self.width))))
        self.cornerRadius = parent.cornerRadius
        self.rad = 2 * self.cornerRadius

        self.fontSize = int(0.4 * self.height)

        if self.cornerRadius > 0.5 * self.width:
            raise ValueError("Error: cornerradius is greater than width.")

        if self.cornerRadius > 0.5 * self.height:
            raise ValueError("Error: cornerradius is greater than height.")

        self.configure(width=self.width, height=self.height)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.draw()

    def draw(self):
        self.delete('all')
        self.create_image(self.width / 2, self.height / 2, image=self.img)

    def sunken_draw(self):
        self.create_polygon((0, self.height,
                             0, self.height*0.6,
                             self.width/2, self.height), fill=self.parent.release_colour, outline='')
    def printt(self):
        print('fhjd')

    def _on_release(self, event=None):
        self.delete('all')
        #self.img = ImageTk.PhotoImage(
         #   Image.open("image/QuestionM.png").resize((int(0.9 * self.width), int(0.9 * self.width))))
        self.sunken_draw()
        if self.command is not None:
            self.command()
