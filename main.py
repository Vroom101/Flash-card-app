"""
A flashcard application for learning French words.

This application displays French words as flashcards. Users can flip the cards
to see the English translation and mark words as "known" to remove them from
the learning list. The progress is saved to a CSV file.
"""
import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


class FlashCardApp:
    """
    A class to represent the Flashcard Application.

    This class encapsulates the entire functionality of the flashcard application,
    including the user interface, card logic, and data handling.

    Attributes
    ----------
    window : Tk
        The main window of the application.
    canvas : Canvas
        The canvas where the flashcards are displayed.
    to_learn : list
        A list of dictionaries, where each dictionary is a word to learn.
    current_card : dict
        The current word being displayed.
    flip_timer : str
        The timer for flipping the card.
    front_side_img : PhotoImage
        The image for the front of the card.
    back_side_img : PhotoImage
        The image for the back of the card.
    card_background : int
        The image item on the canvas.
    card_title : int
        The text item for the card title.
    card_word : int
        The text item for the card word.

    Methods
    -------
    next_card():
        Displays the next flashcard.
    flip_card():
        Flips the current flashcard to show the English translation.
    is_known():
        Marks the current word as known.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the FlashCardApp object
        and sets up the UI.
        """
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.to_learn = self._load_words()
        self.current_card = {}

        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.front_side_img = PhotoImage(file="images/card_front.png")
        self.back_side_img = PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(400, 263, image=self.front_side_img)
        self.card_title = self.canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2)

        cross_image = PhotoImage(file="images/wrong.png")
        self.unknown_button = Button(image=cross_image, highlightthickness=0, command=self.next_card)
        self.unknown_button.grid(row=1, column=0)

        check_image = PhotoImage(file="images/right.png")
        self.known_button = Button(image=check_image, highlightthickness=0, command=self.is_known)
        self.known_button.grid(row=1, column=1)

        self.flip_timer = self.window.after(3000, self.flip_card)
        self.next_card()

        self.window.mainloop()

    def _load_words(self):
        """Loads words from a CSV file.

        Tries to load words from 'data/words_to_learn.csv'. If the file is
        not found, it loads words from 'data/french_words.csv'.

        Returns:
            list: A list of dictionaries, where each dictionary represents a word.
        """
        try:
            data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            original_data = pandas.read_csv("data/french_words.csv")
            return original_data.to_dict(orient="records")
        else:
            return data.to_dict(orient="records")

    def next_card(self):
        """Displays the next flashcard.

        This function cancels any pending card flip, selects a random word from
        the `to_learn` list, and updates the canvas to show the French word.
        It also schedules the card to be flipped to the English side after 3 seconds.
        """
        self.window.after_cancel(self.flip_timer)
        self.current_card = random.choice(self.to_learn)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_card["French"], fill="black")
        self.canvas.itemconfig(self.card_background, image=self.front_side_img)
        self.flip_timer = self.window.after(3000, self.flip_card)

    def flip_card(self):
        """Flips the current flashcard to show the English translation.

        Updates the canvas to display the English translation of the current word.
        """
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_card["English"], fill="white")
        self.canvas.itemconfig(self.card_background, image=self.back_side_img)

    def is_known(self):
        """Marks the current word as known.

        Removes the current word from the `to_learn` list, saves the updated list
        to `data/words_to_learn.csv`, and displays the next card.
        """
        self.to_learn.remove(self.current_card)
        data = pandas.DataFrame(self.to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        self.next_card()


if __name__ == "__main__":
    app = FlashCardApp()
