from tkinter import *

class CompartmentButton(Canvas):
    def __init__(self, compartment):
        self.compartment = compartment
        Canvas.__init__(self, self.compartment.parent.window, borderwidth=0,
                           relief="flat", highlightthickness=0, bg=self.compartment.parent.panel_bg)
        self.command = lambda: self.compartment.parent.selected.set(compartment.index)
        self.width = 0.4 * self.compartment.parent.width
        self.height = 0.1 * self.compartment.parent.height
        self.cornerRadius = self.compartment.parent.cornerRadius
        self.colour_release = compartment.parent.release_colour
        self.colour_sunken = compartment.parent.sunken_colour
        self.text_bg = "#366359"
        self.rad = 2 * self.cornerRadius

        self.fontSize = int(0.4 * self.height)

        if self.cornerRadius > 0.5 * self.width:
            raise ValueError("Error: cornerradius is greater than width.")

        if self.cornerRadius > 0.5 * self.height:
            raise ValueError("Error: cornerradius is greater than height.")

        self.draw(self.colour_release)
        self.configure(width=self.width, height=self.height)
        self.bind("<ButtonPress-1>", self.press)

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

        self.create_polygon((self.width * 0.56, self.height * 0.8 - self.cornerRadius,
                             self.width * 0.56, self.height * 0.2 + self.cornerRadius,
                             self.width * 0.56 + self.cornerRadius, self.height * 0.2,
                             self.width * 0.86 - self.cornerRadius, self.height * 0.2,
                             self.width * 0.86, self.height * 0.2 + self.cornerRadius,
                             self.width * 0.86, self.height * 0.8 - self.cornerRadius,
                             self.width * 0.86 - self.cornerRadius, self.height * 0.8,
                             self.width * 0.56 + self.cornerRadius, self.height * 0.8),
                            fill=self.text_bg, outline='')

        self.create_arc(
            (self.width * 0.56, self.rad + self.height * 0.2, self.rad + self.width * 0.56, self.height * 0.2),
            start=90, extent=90, fill=self.text_bg, outline='')
        self.create_arc(
            (self.width * 0.86 - self.rad, self.height * 0.2, self.width * 0.86, self.height * 0.2 + self.rad),
            start=0, extent=90, fill=self.text_bg, outline='')
        self.create_arc(
            (self.width * 0.86, self.height * 0.8 - self.rad, self.width * 0.86 - self.rad, self.height * 0.8),
            start=270, extent=90, fill=self.text_bg, outline='')
        self.create_arc(
            (self.width * 0.56, self.height * 0.8 - self.rad, self.width * 0.56 + self.rad, self.height * 0.8),
            start=180, extent=90, fill=self.text_bg, outline='')

        self.draw_text()

    def draw_text(self):
        self.index_text = self.create_text(0.046 * self.width, self.height / 2, text=self.compartment.index+1,
                         fill=self.text_bg, font=('Castoro', self.fontSize), anchor=W)
        self.spice_text = self.create_text(0.165 * self.width, self.height / 2, text=self.compartment.spice,
                         fill="black", font=('Castoro', self.fontSize - 2), anchor=W)
        self.amount_text = self.create_text(0.70*self.width, self.height/2, text="{:.2f}".format(self.compartment.amount),
                         fill='white', font=('Castoro', self.fontSize-3), anchor=E)
        self.metric_text = self.create_text(0.72 * self.width, self.height / 2, text=self.compartment.metric,
                         fill='white', font=('Castoro', self.fontSize-3), anchor=W)

    def delete_text(self):
        self.delete(self.index_text)
        self.delete(self.spice_text)
        self.delete(self.amount_text)
        self.delete(self.metric_text)

    def press(self, event=None):
        self.compartment.parent.compartments[self.compartment.parent.selected.get()].button.draw(self.colour_release)
        self.draw(self.colour_sunken)
        if self.command is not None:
            self.command()
