# Midnight Rider
import sys
import textwrap
import time
import Midnight_Rider_Text


# A text-based game of intrigue and illusion

class Game:

    """Represents our game engine
    attribute:
        done: Describes if the game is
                finished or not- bool

    """
def __init__(self):
        self.done = False

def introduction(self) -> None:
    # TODO: print this out character by character
    typewriter_effect(Midnight_Rider_Text.INTRODUCTION)

def typewriter_effect(self, text: str) -> None:
    for char in textwrap.dedent(text):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

def show_choices(self) -> None:
    time.sleep(1)
    print(Midnight_Rider_Text.CHOICES)
    time.sleep(1)

def get_choice(self) -> None:
    """Gets the user's choice and changes
    the enviroment"""
    # Get the user's response
    user_choice = input().strip(",.?!").lower()

    # based on their choice, change the attribute
    # of the class
    if user_choice == "Q":
        self.done == True

def main() -> None:
    game = Game()
    game.introduction


    # Main Loop
    while not game.done:
        game.show_choices()
        game.get_choice()
        # TODO: Check win/lose conditions

    if __name__  == "__main__":
        main()