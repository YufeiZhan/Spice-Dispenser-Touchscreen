from tkinter import *


class HelpMessage(Canvas):
    def __init__(self, parent, command):
        self.parent = parent
        Canvas.__init__(self, self.parent.window, borderwidth=0,
                        relief="flat", highlightthickness=0, bg=self.parent.panel_bg)
        self.command = command
        self.width = self.parent.width * 0.2
        self.height = self.parent.height * 0.2
        self.cornerRadius = self.parent.cornerRadius
        self.colour_release = self.parent.release_colour
        self.rad = 2 * self.cornerRadius

        self.fontSize = int(0.4 * self.height)

        if self.cornerRadius > 0.5 * self.width:
            raise ValueError("Error: cornerradius is greater than width.")

        if self.cornerRadius > 0.5 * self.height:
            raise ValueError("Error: cornerradius is greater than height.")

        self.configure(width=self.width, height=self.height)
        self.bind("<ButtonRelease-1>", self.release)
        self.draw()

    def draw(self):
        colour = self.colour_release
        self.create_polygon((0, self.height - self.cornerRadius,
                             0, self.cornerRadius,
                             self.cornerRadius, 0,
                             self.width - self.cornerRadius, 0,
                             self.width, self.cornerRadius,
                             self.width, self.height - self.cornerRadius,
                             self.width - self.cornerRadius, self.height,
                             self.cornerRadius, self.height),
                            fill=colour, outline='')

        self.create_arc((0, self.rad, self.rad, 0), start=90, extent=90,
                        fill=colour, outline='')
        self.create_arc((self.width - self.rad, 0, self.width, self.rad), start=0, extent=90,
                        fill=colour, outline='')
        self.create_arc((self.width, self.height - self.rad, self.width - self.rad, self.height), start=270, extent=90,
                        fill=colour, outline='')
        self.create_arc((0, self.height - self.rad, self.rad, self.height), start=180, extent=90,
                        fill=colour, outline='')

    def release(self, event):
        self.place_forget()
        if self.command is not None:
            self.command()
