# Standard Imports
import random

# Local App Imports
from Classes.Game import Game

# Global Vars

with open("./Resources/Words.txt", 'r') as file:
    word_list = [word.replace('\n', '') for word in file.readlines()]  # List Comprehension

word_rnd = random.choice(word_list)

wrongs = []

all_guesses = []

drawing = [
    """     +-----+
           |
           |
           |
           |
           |
    ========""",

    """     +-----+
     |     |
           |
           |
           |
           |
    ========""",

    """     +-----+
     |     |
     O     |
           |
           |
           |
    ========""",

    """     +-----+
     |     |
     O     |
     |     |
           |
           |
    ========""",

    """     +-----+
     |     |
     O     |
    /|     |
           |
           |
    ========""",

    """     +-----+
     |     |
     O     |
    /|\\    |
           |
           |
    ========""",

    """     +-----+
     |     |
     O     |
    /|\\    |
      \\    |
           |
    ========""",

    """     +-----+
     |     |
     O     |
    /|\\    |
    / \\    |
           |
    ========"""
]

drawing_index = 0


# Function Definitions

def inputValidation(guesses_list):
    """
    This function will validate the input of the game. It verifies that the input doesn't
    take any digit, repeated or used letters or multiple characters as a value. In case of
    any of these occurrences it prompts the error message and proceeds to ask the user
    again for the input.

    :param guesses_list:
    :return:
    """
    while True:
        letter = input('Type a letter to match the hidden word. (Try not to use repeated letters) \n')

        if len(letter) > 1 or len(letter) == 0:
            print("The input max length is 1 character, please try again.")
            continue
        elif letter.isdigit():
            print("The input can't contain any number value.")
            continue
        elif letter in guesses_list:
            print("This character has already been used, please type another one.")
            continue
        else:
            break
    return letter


# Object Initialization
Game = Game(word_rnd)

print(drawing[0])
print("Word: %s" % Game.showBlanks())
blankedWord = Game.showBlanks()

# Len function brings the length of the list, we use the -1 so we can
# properly work with Python indexing

while drawing_index < len(drawing) - 1:
    guess = inputValidation(all_guesses)

    if Game.Matched(guess):
        print(drawing[drawing_index])
        blankedWord = Game.showGuess(guess, blankedWord)
        print("Word: %s" % blankedWord)
        if "_" not in blankedWord:  # Winning exit condition
            print("Congratulations! You won the game!. Run the script to play again!")
            break
    else:
        drawing_index += 1
        print(drawing[drawing_index])
        print("Word: %s" % blankedWord)
        wrongs.append(guess)
        if drawing_index == len(drawing) - 1:  # Loosing exit condition
            print("Oh shoot! You lost this one, but you can always win the next one. Run the script to play again!")
            exit()

    all_guesses.append(guess)

    print("List of wrong letters: " + ", ".join(wrongs))
