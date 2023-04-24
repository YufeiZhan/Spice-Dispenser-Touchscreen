from tkinter import *

class CompartmentButton(Canvas):
    def __init__(self, compartment):
        self.compartment = compartment
        Canvas.__init__(self, self.compartment.parent.window, borderwidth=0,
                           relief="flat", highlightthickness=0, bg=self.compartment.parent.release_colour)
        self.command = lambda: self.compartment.parent.selected.set(compartment.index)
        self.width = 0.4 * self.compartment.parent.width
        self.height = 0.07 * self.compartment.parent.height
        self.cornerRadius = self.compartment.parent.cornerRadius
        self.colour_release = '#8DA88D'
        self.colour_sunken = '#6D906E'
        self.text_bg = "#366359"
        self.rad = 2 * self.cornerRadius

        self.fontSize = int(0.6 * self.height)

        if self.cornerRadius > 0.5 * self.width:
            raise ValueError("Error: cornerradius is greater than width.")

        if self.cornerRadius > 0.5 * self.height:
            raise ValueError("Error: cornerradius is greater than height.")

        self.draw(self.colour_release)
        self.configure(width=self.width, height=self.height)
        self.bind("<ButtonPress-1>", self.press)
        self.selected = False

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

        self.draw_text()

    def draw_text(self):
        self.spice_text = self.create_text(0.165 * self.width, 0.6*self.height, text=self.compartment.spice,
                         fill="black", font=('Castoro', self.fontSize - 2), anchor=W)
        self.amount_text = self.create_text(0.70*self.width, 0.6*self.height, text="{:.2f}".format(self.compartment.amount),
                         fill='black', font=('Castoro', self.fontSize-3), anchor=E)
        self.metric_text = self.create_text(0.72 * self.width, 0.6*self.height, text=self.compartment.metric,
                         fill='black', font=('Castoro', self.fontSize-3), anchor=W)

    def delete_text(self):
        self.delete(self.index_text)
        self.delete(self.spice_text)
        self.delete(self.amount_text)
        self.delete(self.metric_text)

    def press(self, event=None):
        if not self.selected:
            self.draw(self.colour_sunken)
        else:
            self.draw(self.colour_release)
        self.selected = not self.selected
        if self.command is not None:
            self.command()
