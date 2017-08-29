# -*- coding: utf-8 -*-
from random import sample, randint
from tkinter import Label, Canvas

from app import *


class Conveyor(Frame):
    def __init__(self, master, picture, width):
        super().__init__()
        self.master = master  # App is parent.
        self.picture = picture  # App.resized_picture
        self.width = width  # Width of main table = 4
        self.n = width * (width - 1) + 1  # Number of images to show on conveyor = 13
        self.image_number_list = []  # Index list after shuffling App.resized_picture
        self.labels = []  # Label widget list for conveyor
        self.image_flags = list(
            False for i in range(self.width * self.width)
        )  # Check if image is on conveyor. Default is False.

        # Shuffle self.picture (= App.resized_picture)
        self.random_shuffle()

        # TODO
        # Create image labels.
        for i in range(self.n):
            pic_label = Label(self, image=self.picture[self.image_number_list[i]])
            # Put labels on the conveyor.
            pic_label.grid(row=1, column=i)
            # Save labels in the list labels.
            self.labels.append(pic_label)
            # Make sure label is on the conveyor.
            self.image_flags[self.image_number_list[i]] = True

        # Set current index = start location
        self.cur_idx = int(self.n / self.width * (self.width - 1))

        # Set current image = start image location
        # Assign to compare with selected image on the main table.
        self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])

        # TODO
        # Set canvas.
        # Create canvas widget for index marker.
        self.canvas_marker = Canvas(self, width=30, height=30)
        # Create index marker.
        self.canvas_marker.create_polygon((2, 10), (30, 10), (16, 30), fill='yellow', outline='black')
        # Grid canvas.
        self.canvas_marker.grid(row=0, column=9)
        # Create canvas widget for text Final.
        self.canvas_text = Canvas(self, width=35, height=20)
        # Create text.
        self.text = self.canvas_text.create_text(20, 15, text='FINAL', fill='Red', font='Helvetica 12 bold')
        # Grid canvas.
        self.canvas_text.grid(row=0, column=12)

    # TODO
    def random_shuffle(self):
        """Create a list of shuffled indices of self.picture."""
        self.image_number_list = sample(range(self.width * self.width), self.n)

    # TODO
    def correct_match(self):
        """When selected image and conveyor image are a match"""
        # When it was the last image
        if self.cur_idx == self.n - 1:
            self.master.quit_game(win=True)
        else:
            if self.cur_idx == self.n - 2:
                self.cur_idx += 1
                self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
                self.canvas_marker.grid(row=0, column=self.cur_idx)
            else:
                self.cur_idx += 1
                self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
                self.canvas_marker.grid(row=0, column=self.cur_idx)

    # TODO
    def wrong_match(self):
        """When selected image and conveyor image are not a match"""
        # When it was the first image
        if self.cur_idx == 0:
            self.master.quit_game(win=False)
        else:
            if self.cur_idx == self.n - 1:
                self.cur_idx -= 1
                self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
                self.canvas_marker.grid(row=0, column=self.cur_idx)
            else:
                self.cur_idx -= 1
                self.canvas_marker.grid(row=0, column=self.cur_idx)

            # Get new image
            while True:
                new_image = randint(0, self.width * self.width - 1)
                if new_image not in self.image_number_list:
                    break

            # Move image to left
            for i in range(0, self.n - 1):
                self.labels[i].config(image=self.picture[self.image_number_list[i + 1]])
                self.image_number_list[i] = self.image_number_list[i + 1]

            # Add new image to conveyor
            self.image_number_list[self.n - 1] = new_image
            self.labels[self.n - 1].config(image=self.picture[self.image_number_list[self.n - 1]])
