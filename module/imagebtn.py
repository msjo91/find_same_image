# -*- coding: utf-8 -*-
from tkinter import Button


class ImageButton(Button):
    """
    A blueprint for button to grid on the main table.
    The button will have an alphabet on front and a picture hidden.
    """

    def __init__(self, parent=None, **kwargs):
        Button.__init__(self, parent, **kwargs)

    def add_hidden(self, alphabet, hidden):
        """Add hidden image in the widget"""
        self.alphabet = alphabet
        self.hidden = hidden

    def get_hidden(self):
        """Return the widget's hidden image"""
        return self.hidden
