import tkinter as tk

class SearchButton(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent.window, borderwidth=0,
                           relief="flat", highlightthickness=0, bg='white')
        self.command = None
        self.parent = parent
        self.width = 0.86*parent.width
        self.height = 0.08 * self.parent.height
        self.cornerRadius = parent.cornerRadius
        self.rad = 2 * self.cornerRadius
        self.colour_release = parent.release_colour
        self.colour_sunken = parent.sunken_colour
        self.configure(width=self.width, height=self.height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.draw(self.colour_release)

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

    def _on_press(self, event):
        self.draw(self.colour_sunken)


    def _on_release(self, event):
        self.draw(self.colour_release)
        if self.command is not None:
            self.command()
