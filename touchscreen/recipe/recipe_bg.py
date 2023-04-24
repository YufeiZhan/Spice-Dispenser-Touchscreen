from tkinter import *

class RecipeBackground(Canvas):
    def __init__(self, parent):
        Canvas.__init__(self, parent.window, borderwidth=0,
                           relief="flat", highlightthickness=0, bg='white')
        self.parent = parent
        self.width = 0.42 * parent.width
        self.height = 0.69 * parent.height
        self.cornerRadius = parent.cornerRadius
        self.rad = 2 * self.cornerRadius
        self.configure(width=self.width, height=self.height)
        self.draw(self.parent.release_colour)

    def draw(self, colour):
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


    def drawText(self):
        self.create_line(0.03 * self.width, 0.075 * self.height,
                                0.97 * self.width, 0.075 * self.height,
                                fill='#164A41')

        self.create_text(0.13 * self.width, 0.09 * self.height,
                                anchor=SW, text='Spice Name', fill='#164A41',
                                font=('Castoro', int(0.048 * self.height)))

        self.create_text(0.6 * self.width, 0.09 * self.height,
                                anchor=SW, text='Amount', fill='#164A41',
                                font=('Castoro', int(0.048 * self.height)))
