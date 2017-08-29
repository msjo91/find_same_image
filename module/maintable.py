# -*- coding: utf-8 -*-
from random import sample
from time import sleep

from app import *
from imagebtn import ImageButton


class Maintable(Frame):
    n = 0
    selected_image = 0

    def __init__(self, master, picture, alphabet, width):
        super().__init__()
        self.master = master  # App is parent
        self.picture = picture  # App.picture_image
        self.alphabet = alphabet  # App.alphabet_image
        self.width = width  # Width of main table = 4
        self.n = width * width  # Number of images to be used in main table = 16
        self.image_number_list = []  # Index list after shuffling App.picture_image

        # Shuffle App.picture_image (= hidden image)
        self.random_shuffle()

        # TODO
        # Create ImageButton widget with alphabet image
        btn_list = []
        for i in range(self.width):
            for j in range(self.width):
                idx = self.image_number_list.pop()
                btn_list.append(ImageButton(self, image=self.alphabet[idx]))
                btn_list[-1].grid(row=i, column=j)
                # Add hidden image
                btn_list[-1].add_hidden(
                    alphabet=self.alphabet[idx],
                    picture=self.picture[idx])
                # Bind click event
                btn_list[-1].bind('<ButtonPress-1>', self.click_event)

    # TODO
    def random_shuffle(self):
        """Create a list of shuffled self.picture indices."""
        self.image_number_list = sample(range(self.n))

    def show_hidden(self, event):
        """Event handler: show hidden image"""
        event.widget.config(image=event.widget.get_hidden())

    # TODO
    def hide_picture(self, event):
        """
        Event handler:
        1. Hide hidden image and recall alphabet.
        2. Compare the selected image with the current conveyor image.
        3. Run appropriate function according to match result.
        """
        selected_image = self.picture.index(event.widget.hidden)
        event.widget.config(image=event.widget.alphabet)
        if selected_image == self.master.conveyor.image_number_list[self.master.conveyor.cur_idx]:
            self.master.conveyor.correct_match()
        else:
            self.master.conveyor.wrong_match()

    def click_event(self):
        self.show_hidden()
        self.after(300)
        self.hide_picture()
