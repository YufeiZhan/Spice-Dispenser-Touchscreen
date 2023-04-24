'''
The entry file where the app is initiated.
'''

# import external libraries
from tkinter import *

# import helper files
from keyboard import Keyboard
from main.main_compartment import Compartment
from main.main_funtion_button import FunctionButton
from main.main_help_button import HelpButton
from main.main_help_message import HelpMessage


class MainPage():
    def __init__(self, parent):
        self.window = parent.window
        self.width = parent.width
        self.height = parent.height
        self.canvas = parent.canvas
        self.cornerRadius = parent.cornerRadius

        # Colour
        self.panel_bg = parent.panel_bg
        self.release_colour = parent.release_colour
        self.sunken_colour = parent.sunken_colour
        self.amount_bg = parent.amount_bg

        # Compartment section
        self.selected = IntVar()

        self.compartment_size = 6
        self.compartments = []
        for i in range(self.compartment_size):
            self.compartments.append(Compartment(self, i))

        names = ["Salt", "Peper", "Cumin", "Five Spice", "Chillie", "Ginger"]
        for i in range(len(names)):
            self.compartments[i].add_spice(names[i])

        # - Quantity
        self.quantity_buttons = []
        self.quantity_buttons.append(FunctionButton(self, command=self.resetQuantity, img_path='reset_button.png'))
        self.quantity_buttons.append(FunctionButton(self, command=self.decreaseQuantity, img_path='decrease_0.25_button.png'))
        self.quantity_buttons.append(FunctionButton(self, command=self.increaseQuantity, img_path='increase_0.25_button.png'))
        self.quantity_buttons.append(FunctionButton(self, command=self.fastIncreaseQuantity, img_path='increase_1_button.png'))

        # - Metric
        self.metric_buttons = []
        self.metric_buttons.append(FunctionButton(self, command=self.setDash, img_path='dash_button.png'))
        self.metric_buttons.append(FunctionButton(self, command=self.setPinch, img_path='pinch_button.png'))
        self.metric_buttons.append(FunctionButton(self, command=self.setTSP, img_path='teaspoon_button.png'))
        self.metric_buttons.append(FunctionButton(self, command=self.setTBSP, img_path='tablespoon_button.png'))

        # - Control
        self.control_buttons = []
        # self.control_buttons.append(FunctionButton(self, command=self.edit, img_path='edit_button.png'))
        self.control_buttons.append(FunctionButton(self, command=self.clearAll, img_path='clear_button.png'))
        self.control_buttons.append(FunctionButton(self, command=self.decreaseQuantity, img_path='ready_button.png'))

        # - Help
        self.help_buttons = []
        self.help_messages = []
        self.help_buttons.append(HelpButton(self, command=self.draw_message_box_0))
        self.help_messages.append(HelpMessage(self, command=self.help_buttons[0].draw))
        self.help_buttons.append(HelpButton(self, command=self.draw_message_box_1))
        self.help_messages.append(HelpMessage(self, command=self.help_buttons[1].draw))
        self.help_buttons.append(HelpButton(self, command=self.draw_message_box_2))
        self.help_messages.append(HelpMessage(self, command=self.help_buttons[2].draw))
        self.help_buttons.append(HelpButton(self, command=self.draw_message_box_3))
        self.help_messages.append(HelpMessage(self, command=self.help_buttons[3].draw))
        self.help_buttons.append(HelpButton(self, command=self.draw_message_box_4))
        self.help_messages.append(HelpMessage(self, command=self.help_buttons[4].draw))

    # Reaction Functions & Helper Functions
    def drawSpiceSelection(self):
        for i in range(self.compartment_size):
            self.compartments[i].button.place(relx=0.1, rely=0.2 + 0.125 * i, anchor=NW)

        self.compartments[0].button.press()

    def drawQuantitySelection(self):
        for i in range(len(self.quantity_buttons)):
            self.quantity_buttons[i].place(relx=0.55 + 0.1 * i, rely=0.18, anchor=NW)

    def drawMetricSelection(self):
        for i in range(len(self.metric_buttons)):
            self.metric_buttons[i].place(relx=0.55 + 0.1 * i, rely=0.457, anchor=NW)

    def drawControl(self):
        for i in range(len(self.control_buttons)):
            self.control_buttons[i].place(relx=0.6 + 0.1 * i, rely=0.733, anchor=NW)

    def drawText(self):
        self.canvas.create_line(0.1 * self.width, 0.17 * self.height,
                                (0.1 + 0.4) * self.width, 0.17 * self.height,
                                fill='#164A41')

        self.canvas.create_text(0.14 * self.width, 0.17 * self.height,
                                anchor=SW, text='Spice Name', fill='#164A41',
                                font=('Castoro', int(0.035 * self.height)))

        self.canvas.create_text(0.343 * self.width, 0.17 * self.height,
                                anchor=SW, text='Amount', fill='#164A41',
                                font=('Castoro', int(0.035 * self.height)))

        self.canvas.create_text(0.743 * self.width, 0.17 * self.height,
                                anchor=S, text='Quantity', fill='#164A41',
                                font=('Castoro', int(0.035 * self.height)))

        self.help_buttons[0].place(relx=0.808, rely=0.17, anchor=S)

        self.canvas.create_text(0.743 * self.width, 0.447 * self.height,
                                anchor=S, text='Metric', fill='#164A41',
                                font=('Castoro', int(0.035 * self.height)))

        self.help_buttons[1].place(relx=0.795, rely=0.447, anchor=S)

        self.canvas.create_text(0.643 * self.width, 0.723 * self.height,
                                anchor=S, text='Edit', fill='#164A41',
                                font=('Castoro', int(0.035 * self.height)))

        self.help_buttons[2].place(relx=0.682, rely=0.723, anchor=S)

        self.canvas.create_text(0.743 * self.width, 0.723 * self.height,
                                anchor=S, text='Clear', fill='#164A41',
                                font=('Castoro', int(0.035 * self.height)))

        self.help_buttons[3].place(relx=0.787, rely=0.723, anchor=S)

        self.canvas.create_text(0.843 * self.width, 0.723 * self.height,
                                anchor=S, text='Ready', fill='#164A41',
                                font=('Castoro', int(0.035 * self.height)))

        self.help_buttons[4].place(relx=0.892, rely=0.723, anchor=S)

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

    # def edit(self):
        # Keyboard(self)

    def clear(self):
        self.canvas.delete('all')
        for compartment in self.compartments:
            compartment.button.place_forget()

        for button in self.quantity_buttons + self.metric_buttons + self.control_buttons:
            button.place_forget()

        for help in self.help_messages:
            help.release(help)

        for help_button in self.help_buttons:
            help_button.place_forget()

    def draw_message_box_0(self):
        self.help_messages[0].place(relx=0.808, rely=0.17, anchor=N)

    def draw_message_box_1(self):
        self.help_messages[1].place(relx=0.795, rely=0.447, anchor=N)

    def draw_message_box_2(self):
        self.help_messages[2].place(relx=0.682, rely=0.723, anchor=N)

    def draw_message_box_3(self):
        self.help_messages[3].place(relx=0.787, rely=0.723, anchor=N)

    def draw_message_box_4(self):
        self.help_messages[4].place(relx=0.892, rely=0.723, anchor=N)

    def draw(self):
        self.drawSpiceSelection()
        self.drawQuantitySelection()
        self.drawMetricSelection()
        self.drawControl()
        self.drawText()
