'''
The entry file where the app is initiated.
'''

# import external libraries
from tkinter import *

# import helper files
from main_compartment import Compartment
from main_funtion_button import FunctionButton
from recipe_search_button import SearchButton
from recipe_bg import RecipeBackground

from main_compartment_button import CompartmentButton

FIRST_COMPARTMENT_X = 0.1

FIRST_COMPARTMENT_Y = 0.2

COMPARTMENT_INTERVAL_Y = 0.12


class RecipePage():
    def __init__(self, parent):
        self.window = parent.window
        self.panel_bg = parent.panel_bg
        self.width = parent.width
        self.height = parent.height
        self.canvas = parent.canvas

        # Colour
        self.release_colour = '#B7C9B7'
        self.sunken_colour = '#82A083'
        self.amount_bg = "#366359"

        # Compartment section
        self.selected = IntVar()

        self.compartment_size = 6
        self.compartments = []
        for i in range(self.compartment_size):
            self.compartments.append(Compartment(self, i))

        names = ["Salt","Peper","Cumin","Five Spice","Chillie","Ginger"]
        for i in range(len(names)):
            self.compartments[i].add_spice(names[i])

        # - Search
        self.search = SearchButton(self)

        # - Background
        self.background_left = RecipeBackground(self)
        self.background_right = RecipeBackground(self)

        # - Metric
        self.metric_buttons = []
        self.metric_buttons.append(FunctionButton(self, command=self.setDash, img_path='dash_button.png'))
        self.metric_buttons.append(FunctionButton(self, command=self.setPinch, img_path='pinch_button.png'))
        self.metric_buttons.append(FunctionButton(self, command=self.setTSP, img_path='teaspoon_button.png'))
        self.metric_buttons.append(FunctionButton(self, command=self.setTBSP, img_path='tablespoon_button.png'))

        # - Control
        self.control_buttons = []
        self.control_buttons.append(FunctionButton(self, command=self.decreaseQuantity, img_path='edit_button.png'))
        self.control_buttons.append(FunctionButton(self, command=self.clearAll, img_path='clear_button.png'))
        self.control_buttons.append(FunctionButton(self, command=self.decreaseQuantity, img_path='ready_button.png'))

    # Reaction Functions & Helper Functions
    def drawSpiceSelection(self):
        for i in range(self.compartment_size):
            self.compartments[i].button.place(relx=FIRST_COMPARTMENT_X, rely=FIRST_COMPARTMENT_Y + COMPARTMENT_INTERVAL_Y * i, anchor=NW)

        self.compartments[0].button.press()

    def drawQuantitySelection(self):
        for i in range(len(self.quantity_buttons)):
            self.quantity_buttons[i].place(relx=0.55 + 0.1 * i, rely=0.2, anchor=NW)

    def drawMetricSelection(self):
        for i in range(len(self.metric_buttons)):
            self.metric_buttons[i].place(relx=0.55 + 0.1 * i, rely=0.457, anchor=NW)

    def drawControl(self):
        for i in range(len(self.control_buttons)):
            self.control_buttons[i].place(relx=0.6 + 0.1 * i, rely=0.714, anchor=NW)

    def drawText(self):
        self.canvas.create_line(FIRST_COMPARTMENT_X * self.width, 0.17 * self.height,
                                (FIRST_COMPARTMENT_X + 0.4) * self.width, 0.17 * self.height,
                                fill='#164A41')

        self.canvas.create_text((FIRST_COMPARTMENT_X + 0.04) * self.width, 0.17 * self.height,
                                anchor=SW, text='Spice Name', fill='#164A41',
                                font=('Castoro', int(0.045 * self.height)))

        self.canvas.create_text((FIRST_COMPARTMENT_X + 0.243) * self.width, 0.17 * self.height,
                                anchor=SW, text='Amount', fill='#164A41',
                                font=('Castoro', int(0.045 * self.height)))

        self.canvas.create_text(0.743 * self.width, 0.185 * self.height,
                                anchor=S, text='Quantity', fill='#164A41',
                                font=('Castoro', int(0.045 * self.height)))

        self.canvas.create_text(0.743 * self.width, 0.442 * self.height,
                                anchor=S, text='Metrc', fill='#164A41',
                                font=('Castoro', int(0.045 * self.height)))

        self.canvas.create_text(0.643 * self.width, 0.699 * self.height,
                                anchor=S, text='Edit', fill='#164A41',
                                font=('Castoro', int(0.045 * self.height)))

        self.canvas.create_text(0.743 * self.width, 0.699 * self.height,
                                anchor=S, text='Clear', fill='#164A41',
                                font=('Castoro', int(0.045 * self.height)))

        self.canvas.create_text(0.843 * self.width, 0.699 * self.height,
                                anchor=S, text='Ready', fill='#164A41',
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
