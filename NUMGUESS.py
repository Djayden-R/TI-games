from random import *

"""
Number Guessing game

Version: 1.2

Made by:
    DjaydenR
    
Description:
    A simple game where you need to guess a number between 1 and 100.
    Adjust the range of numbers below. 
    
How to share this game: 
    1. Connect two calculator with a cable.
    2. On both calculators, press [2nd] + [x,t,0,n].
    3. On the sending calculator, choose 2: All-... 
    4. On the receiving calculator, press RECEIVE 
    5. Find the game in the file list.
"""

# modify to change difficulty
max_attempts = 25
min_guess = 1
max_guess = 100


def intro():
    print("\n" * 9)
    print("Number guessing game (" + str(min_guess) + "-" + str(max_guess) + ")")
    while True:
        attempts = input("How many tries do you want? ")
        if is_valid(attempts):
            if int(attempts) > max_attempts:
                print("The max amount of attempts is", str(max_attempts))
            else:
                attempts = int(attempts)
                number = randint(min_guess - 1, max_guess + 1)
                return attempts, number


def guessing(attempts, number):
    counter = 1
    while counter <= attempts:
        text_guess = input("Guess " + str(counter) + ": ")
        if is_valid(text_guess):
            guess = int(text_guess)
            if not min_guess <= guess <= max_guess:
                print("Enter a valid number")
            elif guess < number:
                print("The number is higher")
                counter += 1
            elif guess > number:
                print("The number is lower")
                counter += 1
            elif guess == number:
                print("You are correct!")
                break

    else:
        print("Out of guesses")
        print("The number was " + str(number))


def is_valid(value):
    if value.lower() == "stop" or value.lower() == "exit":
        print("Exiting the game.")
        quit()
    else:
        try:
            number = int(value)
        except ValueError:
            print("Please enter a number")
            return False
        else:
            return True


def game():
    while True:
        attempts, number = intro()
        guessing(attempts, number)
        while True:
            play_again = input("Would you like to play again?   (0/1): ")
            if play_again == "0":
                return
            elif play_again == "1":
                break
            else:
                print("Please type a 1 or a 0")


game()