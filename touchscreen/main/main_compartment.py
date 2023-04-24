"""
This is the file for the spice object.

A spice has attribute: name, percentage, chosen quantity and chosen metrics.
"""

from main.main_compartment_button import CompartmentButton

class Compartment:
    def __init__(self, parent, index):
        self.button = None
        self.parent = parent
        self.index = index
        self.spice = None
        self.amount = 0
        self.metric = 'dash'

    def add_spice(self, spice):
        self.spice = spice
        self.button = CompartmentButton(self)

    def update_spice_name(self, str):
        if str == 'enter':
            pass
        elif str == '<--':
            spice = self.spice[:-1]
        else:
            spice = self.spice + str
        self.add_spice(spice)

    def update_amount(self, amount):
        updated_amount = self.amount + amount
        self.amount = (updated_amount > 0) * abs(updated_amount)
        self.button.delete_text()
        self.button.draw_text()

    def update_metric(self, metric):
        self.metric = metric
        self.button.delete_text()
        self.button.draw_text()
