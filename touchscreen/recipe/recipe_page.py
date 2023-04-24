'''
The entry file where the app is initiated.
'''

# import external libraries
from tkinter import *

# import helper files

from recipe.recipe_search_button import SearchButton
from recipe.recipe_bg import RecipeBackground
from recipe.recipe_compartment import Compartment


class RecipePage():
    def __init__(self, parent):
        self.window = parent.window
        self.panel_bg = parent.panel_bg
        self.width = parent.width
        self.height = parent.height
        self.canvas = parent.canvas
        self.cornerRadius = parent.cornerRadius

        # Colour
        self.release_colour = '#B7C9B7'
        self.sunken_colour = '#82A083'
        self.amount_bg = "#366359"

        # - Search
        self.search = SearchButton(self)

        # - Background
        self.background_left = RecipeBackground(self)
        self.background_right = RecipeBackground(self)
        self.background_right.drawText()

        # Compartment section
        self.selected = IntVar()

        self.compartment_size = 6
        self.compartments = []
        for i in range(self.compartment_size):
            self.compartments.append(Compartment(self, i))

        names = ["Salt", "Peper", "Cumin", "Five Spice", "Chillie", "Ginger"]
        for i in range(len(names)):
            self.compartments[i].add_spice(names[i])

    # Reaction Functions & Helper Functions
    def drawSpiceSelection(self):
        for i in range(self.compartment_size):
            self.compartments[i].button.place(relx=0.75, rely=0.3 + 0.09 * i, anchor=N)

    def drawText(self):
        self.background_right.create_line(0.6 * self.width, 0.17 * self.height,
                                (0.6 + 0.4) * self.width, 0.17 * self.height,
                                fill='#164A41')

        self.background_right.create_text(0.5 * self.width, 0.5 * self.height,
                                anchor=SW, text='Spice Name', fill='#164A41',
                                font=('Castoro', int(0.045 * self.height)))

        self.background_right.create_text((0.75 + 0.243) * self.width, 0.17 * self.height,
                                anchor=SW, text='Amount', fill='#164A41',
                                font=('Castoro', int(0.045 * self.height)))

    def decreaseQuantity(self):
        self.compartments[self.selected.get()].update_amount(-0.25)

    def increaseQuantity(self):
        self.compartments[self.selected.get()].update_amount(0.25)

    def resetQuantity(self):
        self.compartments[self.selected.get()].update_amount(-self.compartments[self.selected.get()].amount)

    def fastIncreaseQuantity(self):
        self.compartments[self.selected.get()].update_amount(1)

    def setDash(self):
        self.compartments[self.selected.get()].update_metric('dash')

    def setPinch(self):
        self.compartments[self.selected.get()].update_metric('pinch')

    def setTSP(self):
        self.compartments[self.selected.get()].update_metric('tsp')

    def setTBSP(self):
        self.compartments[self.selected.get()].update_metric('Tbsp')

    def clearAll(self):
        for compartment in self.compartments:
            compartment.update_amount(-compartment.amount)
            compartment.update_metric('dash')

    def clear(self):
        self.canvas.delete('all')
        self.search.place_forget()
        self.background_left.place_forget()
        self.background_right.place_forget()

    def draw(self):
        self.search.place(relx=0.1, rely=0.125)
        self.background_left.place(relx=0.1, rely=0.235)
        self.background_right.place(relx=0.54, rely=0.235)
        self.drawSpiceSelection()
