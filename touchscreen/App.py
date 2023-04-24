from tkinter import *

from main.main_page import MainPage
from recipe.recipe_page import RecipePage
from App_page_button import PageSwitch
from status_bar import StatusBar


class App:
    def __init__(self):
        # Colour
        self.panel_bg = "#FDFFFD"
        self.page_bg = '#4D774E'
        self.release_colour = '#B7C9B7'
        self.sunken_colour = '#82A083'
        self.amount_bg = "#366359"

        # Main window
        self.window = Tk()
        self.width = 800  # self.window.winfo_screenwidth()
        self.height = 400  # self.window.winfo_screenheight()
        self.window.geometry("{}x{}".format(self.width, self.height))
        # self.window.attributes('-fullscreen', True)
        self.window.bind("<Escape>", lambda event: self.window.destroy())
        self.canvas = Canvas(self.window, width=self.width, height=self.height, bg=self.panel_bg, highlightthickness=0)
        self.cornerRadius = 4 * (self.width / self.height)

        self.main_page = MainPage(self)
        self.recipe_page = RecipePage(self)

        self.main_button = PageSwitch(self, command=self.switch_to_main)
        self.recipe_button = PageSwitch(self, command=self.switch_to_recipe)
        self.main_button.press()

        self.bar_canvas = Canvas(self.window, width=self.width, height=0.077 * self.height, bg='#DCDDDC', highlightthickness=0)
        self.bar_canvas.place(x=0, y=0,anchor=NW)
        self.bar = StatusBar(self)


        self.main_button.place(relx=0, rely=0.077)
        self.recipe_button.place(relx=0, rely=0.5385)

        self.canvas.pack()
        self.window.mainloop()

    def switch_to_main(self):
        self.recipe_button.release()
        self.recipe_page.clear()
        self.main_page.draw()

    def switch_to_recipe(self):
        self.main_button.release()
        self.main_page.clear()
        self.recipe_page.draw()


if __name__ == "__main__":
    App()
