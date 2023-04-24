from tkinter import *


class PageSwitch(Canvas):
    def __init__(self, parent, command=None):
        self.parent = parent
        Canvas.__init__(self, self.parent.window, borderwidth=0,
                           relief="flat", highlightthickness=0, bg=self.parent.page_bg)
        self.command = command
        self.width = 0.06 * self.parent.width
        self.height = (0.923 * self.parent.height)/2
        self.cornerRadius = 4 * (
                    self.parent.width / self.parent.height)
        self.colour_release = self.parent.page_bg
        self.colour_sunken = self.parent.panel_bg
        self.rad = 2 * self.cornerRadius

        if self.cornerRadius > 0.5 * self.width:
            raise ValueError("Error: cornerradius is greater than width.")

        if self.cornerRadius > 0.5 * self.height:
            raise ValueError("Error: cornerradius is greater than height.")

        self.draw(self.colour_release)
        self.configure(width=self.width, height=self.height)
        self.bind("<ButtonPress-1>", self.press)

    def draw(self, colour):
        self.create_polygon((0.1*self.width, self.height - self.cornerRadius,
                             0.1*self.width, self.cornerRadius,
                             0.1*self.width+self.cornerRadius, 0,
                             self.width, 0,
                             self.width, self.height,
                             0.1*self.width+self.cornerRadius, self.height),
                            fill=colour, outline=colour)

        self.create_arc((0.1*self.width, self.rad, 0.1*self.width+self.rad, 0), start=90, extent=90,
                        fill=colour, outline=colour)
        self.create_arc((0.1*self.width, self.height - self.rad, 0.1*self.width+self.rad, self.height), start=180, extent=90,
                        fill=colour, outline=colour)

    def release(self):
        self.delete('all')
        self.draw(self.colour_release)

    def press(self, event=None):
        self.delete('all')
        self.draw(self.colour_sunken)
        if self.command is not None:
            self.command()
