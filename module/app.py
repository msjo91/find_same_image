# -*- coding: utf-8 -*-
from tkinter import Frame, PhotoImage, messagebox
from PIL import Image, ImageTk
from conveyor import Conveyor
from maintable import Maintable


class App(Frame):
    """Frames and preps."""
    picture_image = []  # Picture list for main table
    alphabet_image = []  # Alphabet list for main table
    resized_picture = []  # Picture list for conveyor
    continue_game = 1

    def __init__(self, master, n):
        super().__init__()
        self.master = master  # root = Tk() is parent.
        self.n = n
        self.create_images()  # Open, read and write images.

        # Create main table frame widget.
        # master=App(), picture=App.picture_image, alphabet=App.alphabet_image, width=App.n
        self.table = Maintable(self, self.picture_image, self.alphabet_image, self.n)
        # Put it on the first row of the frame.
        self.table.grid(row=0, column=0, pady=(10, 20))

        # Create conveyor frame widget.
        # master=App(), picture=App.resized_picture, width=App.n
        self.conveyor = Conveyor(self, self.resized_picture, self.n)
        # Put it on the second row of the frame.
        self.conveyor.grid(row=1, column=0)

    def create_images(self):
        """
        Read image files, create image objects and save them in list.
        Image objects in the list will not be changed.
        They are only randomized by shuffling indices.
        """
        self.picture_image = list(Image.open("../picture/%d.jpg" % (i + 1)) for i in range(self.n * self.n))
        self.alphabet_image = list(PhotoImage(file="../alphabet/%d.gif" % (i + 1)) for i in range(self.n * self.n))
        self.resized_picture = list(
            self.picture_image[i].resize((50, 50), Image.ANTIALIAS) for i in range(self.n * self.n)
        )
        self.resized_picture = list(ImageTk.PhotoImage(self.resized_picture[i]) for i in range(self.n * self.n))
        self.picture_image = list(ImageTk.PhotoImage(self.picture_image[i]) for i in range(self.n * self.n))

    def quit_game(self, win):
        """Either win or lose the game; then call continue box."""
        if win is True:
            messagebox.showinfo("Game Over", "Success! You win!")
        else:
            messagebox.showinfo("Game Over", "Failed. You lost.")

        result = messagebox.askquestion("Restart", "Restart the game?", icon='warning')
        if result == 'no':
            App.continue_game = 0

        # Close conveyor.
        self.conveyor.quit()
        # Close main table.
        self.table.quit()
        # Close app.
        self.quit()
