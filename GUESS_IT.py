from random import *
from time import *

"""
Guess it

Version: beta 1.2

Made by:
    DjaydenR
    
Description:
    This is a variation on the game hangman, there are 3 different modes to this game:
    1. Enter any word you want.
    2. Select a word out of the five randomly selected words.
    3. You are asked five times if you want to choose a word, after that the last word is chosen.
    The idea is that one person selects a word and the other one guesses the word.
    
How to share this game: 
    1. Connect two calculators using a cable.
    2. On both calculators, press [2nd] + [x,t,0,n].
    3. On the sending calculator, select 2: All-... 
    4. On the receiving calculator, press RECEIVE 
    5. Find the game in the file list and press send.
"""

w = 0.75 #wait time after error messages

PICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORD_LIST = ["Appel", "Boek", "Kat", "Hond", "Auto", "Huis", "Boom", "Ster", "Fiets", "School", "Vliegtuig", "Tafel", "Zomer", "Film", "Tuin", "Muziek", "Strijd", "Avontuur", "Reis", "Maan"]

def sample(list, amount):
    words = []
    indices = set()
    while len(indices) < amount:
        index = randint(0,len(list)-1)
        if index not in indices:
            indices.add(index)
            words.append(list[index])
    return words

def choice_menu():
    error_message = ""
    while True:
        clear(3)
        print(
"""How to select words:

1. Free choice
2. One out of five
3. Five tries to choose
{}""".format(error_message))
        game_mode = input("Select Mode: ")
        if check_input(game_mode, "int", options = ["1", "2", "3"]):
            return game_mode
        
def process_menu():
    game_mode = choice_menu()
    if game_mode == "1":
        while True:
            clear(9)
            word = input("Type a word: ")
            if check_input(word, "str"):
                return word
    
    elif game_mode == "2":
        while True:
            clear(5)
            random_word_list = sample(WORD_LIST, 5)
            for i in range(5):
                print(str(i+1) + "." + random_word_list[i])
            word_index = input("\nChoose one of these words: ")
            if check_input(word_index, "int", ["1", "2", "3", "4", "5"]):
                return random_word_list[int(word_index)-1]

    elif game_mode == "3": 
        clear(5)
        random_word_list = sample(WORD_LIST, 5)
        for i in range(0,5):
            while True:
                clear(6)
                print("Word {} of {}:".format(i+1, 5))
                print("\n" + random_word_list[i] + "\n")
                answer = input("Do you want to choose this word?(0/1): ")
                if answer == "1":
                    return random_word_list[i]
                elif answer == "0":
                    if i == 4:
                        print("No word chosen, last word was", random_word_list[i])
                        sleep(1)
                        return random_word_list[i]
                    else:
                        break
                else:
                    print("Incorrect answer")
                    sleep(1)


def clear(lines):
    print("\n" * lines)

def guessing(word):
    letters_of_word = []
    letters_guessed = set()
    current_stage = 0
    for letter in word:
        letters_of_word.append(letter.lower())
    while True:
        print_statement = ""
        clear(1)
        print(PICS[current_stage])
        for letter in letters_of_word:
                if letter in letters_guessed:
                    print_statement += letter + " "
                else:
                    print_statement += ("_ ")
        print(print_statement)
        if "_" not in print_statement:
            print("Game won!")
            play_again()
            break
        guess = input("Guess a letter: ").lower()
        check_input(guess, "str", max_characters= 1)
        if guess in letters_guessed:
            print("You already guessed this letter")
            sleep(1)
        elif guess.lower() in letters_of_word:
            print("Correct guess")
            sleep(1)
        else:
            print("incorrect guess")
            current_stage += 1
            sleep(1)
        if current_stage == 6:
            print("Game Over")
            print("The word was ", word)
            play_again()
            break
        letters_guessed.add(guess)

def check_input(input, type_of_input, options = None, max_characters = None):
    if input == "":
        print("Input can't be empty")
        sleep(w)
        return False
    elif type_of_input == "int":
        if not input.isdigit():
            print("Only enter a number")
            sleep(w)
            return False
        if options is not None and input not in options:
            print("Number out of range")
            sleep(w)
            return False
        if max_characters is not None and len(input) > max_characters:
            print("Only enter a single number")
            sleep(w)
            return False
        else:
            return True
    elif type_of_input == "str":
        if not input.isalpha():
            print("Only enter letters")
            sleep(w)
            return False
        if max_characters is not None and len(input) > max_characters:
            print(max_characters)
            print("Only enter one letter")
            sleep(w)
            return False
        else:
            return True

def play_again():
    while True:
        answer = input("Do you want to play again? (0/1): ")
        if answer == "1":
            game()
        elif answer == "0":
            print("Ending game...")
            break
        else:
            print("\nEnter either a 1 or 0\n")

def game():
    word = process_menu()
    guessing(word)

game()