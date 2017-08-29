# -*- coding: utf-8 -*-
from tkinter import Button


class ImageButton(Button):
    """
    A blueprint for button to grid on the main table.
    The button will have an alphabet on front and a picture hidden.
    """

    def __init__(self, parent=None, **kwargs):
        super().__init__(self, parent, kwargs)

    # Add hidden image in the widget
    def add_hidden(self, alphabet, hidden):
        self.alphabet = alphabet
        self.hidden = hidden

    # Return the widget's hidden image
    def get_hidden(self):
        return self.hidden
