import random
from termcolor import colored
import sys
import os
import pyfiglet
import fontstyle
import time


def title_ascii():
    """
    ascii art for game title using pyfiglet module
    """
    title_text_ascii = "Word Wander"
    word_wander_ascci_art = pyfiglet.figlet_format(
        title_text_ascii, font='small', justify='center'
    )
    print(word_wander_ascci_art)


def typingeffect(delay, string):
    """
    To create typing effect in command line
    """
    for i in string:
        time.sleep(0.02)
        sys.stdout.write(i)
        sys.stdout.flush()
    if delay == 'yes':
        time.sleep(0.8)  # Delay before printing newline
        sys.stdout.write('\n')
        sys.stdout.flush()


def game_intro():

    """
    Introducing the user to the game, get name, choice of difficulty level,
    and display rules if asked.
    """
    clear_terminal()

    title_ascii()
    print(fontstyle.apply("___a wordle game___\n\n". rjust(50),
                          'bold/blink/yellow'))
    print(fontstyle.apply("Welcome to Word Wander!\n", 'bold'))
    print("Only one way forward: guess the word chosen by the elites.\n\n")
    print("1. Start playing")
    print("2. Check out the Rules")
    print("\n'q' to Quit\n")

    while True:
        menu_choice = input(colored("What is your decision? (1-2)\t",
                                    "light_blue"))
        print()

        if menu_choice.lower() == 'q':
            print("Goodbye!")
            exit()

        if validate_entry("choice", menu_choice):
            break

    if menu_choice == "2":
        game_rules()

    elif menu_choice == "1":
        name = enter_name()
        level = difficulty_level(name)

    return name, level


def enter_name():
    """To allow the user to enter their name and return the value"""

    clear_terminal()
    print("Press 'q' to quit\n\n")
    print(fontstyle.apply(" ".rjust(33) + "Word Wander\n\n".ljust(30), 'bold/yellow'))

    typingeffect('no', "Welcome, brave soul. Many have tried, but none "
                 "have succeeded. Let's see if\nyou're the exception.\n\n")
    typingeffect('no', colored("By what name do you go, human?\n",
                               'light_blue'))
    player_name = input()

    if player_name.lower() == 'q':
        print("Goodbye!")
        exit()

    return player_name


def difficulty_level(player_name):
    """
    To allow the user to choose the difficulty of the game and return the value
    """
    clear_terminal()
    print("Press 'q' to quit\n\n")
    print(fontstyle.apply(" ".rjust(33) + "Word Wander\n\n".ljust(30), 'bold/yellow'))
    print("Choose your difficulty level:\n\n")
    print("1. Simple Mortal - 6 trials")
    print("2. Infinite Intellect - 4 trials")
    print("\n\n")

    while True:
        difficulty_lvl = input(colored("Which of those are you? (1-2):\t",
                                       "light_blue"))
        print()

        if difficulty_lvl.lower() == 'q':
            print("Goodbye!")
            exit()

        if validate_entry("difficulty", difficulty_lvl):
            break

    typingeffect('yes', f"\nYou shall now be tested, {player_name}.")

    return difficulty_lvl


def game_rules():
    """
    Rules of the game thag will appear when called for.
    """
    clear_terminal()
    # print("Press 'q' to quit\n")
    # print(fontstyle.apply("Word Wander\n".rjust(50), 'bold/yellow'))
    print(fontstyle.apply("Instructions:", 'bold/underline'))

    print("\n. The goal is to guess the secret word correctly within "
          "4 or 6 attempts,\n  depending on the chosen difficulty level.\n")
    print(". To make a guess, type in a word of 5 letters and "
          "press enter.\n")
    print(". Every guess must be a valid 5-letter word from the game's "
          "dictionary.\n")
    print(". After each guess, a feedback is provided on the letters "
          "guessed:\n")
    print("   - Correct and in the right position: The letter is highlighted "
          "in " + colored("green", 'green') + ".")
    print("   - Correct and in the wrong position: The letter is highlighted "
          "in " + colored("yellow", 'yellow') + ".")
    print("   - Incorrect: The letter is not highlighted and isn't part "
          "of the secret word.\n")
    print(". You win if you guess the secret word within the allotted "
          "number of attempts,\n  and lose if you fail to do so.\n")
    print(". Once the game is over, you can start a new round and guess "
          "a different\n  secret word.\n")

    while True:
        rule_page_button = input(colored("Press 'b' to go back to game menu an"
                                         "d 'c' to start playing.\n", "blue"))

        if rule_page_button.lower() == "q":
            print("Goodbye!")
            exit()

        if validate_entry("rules", rule_page_button):
            break

    if rule_page_button.lower() == "b":
        main()
    elif rule_page_button.lower() == "c":
        start_game_from_rules()


def validate_entry(type, input):
    """
    Raises ValueError if string value does not match the given choices.
    """

    try:

        if type == "choice":
            if input != "1" and input != "2":
                raise ValueError(
                    "Input value should be '1' or '2' ... or 'q' to quit"
                )

        elif type == "rules":
            if input.lower() != "b" and input.lower() != "c":
                raise ValueError(
                    "Input value should be 'b' or 'c'"
                )
        elif type == "difficulty":
            if input != "1" and input != "2":
                raise ValueError(
                    "Input value should be '1' or '2'"
                )
        elif type == "done":
            if input.lower() != "c" and input.lower() != "b":
                raise ValueError(
                    "Input value should be 'b' or 'c'"
                )

    except ValueError as e:
        print(colored(f"\nInvalid data: {e}.", "red")
              + colored("\nPlease try again. \n", "light_red"))
        return False

    return True


def read_random_word():
    """
    Reads the txt file containg all the words for the game.
    Makes a list of them and randomly chooses a word.
    """
    with open("wordlibrary.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)


def validate_word(word):
    """ Checks if the word entered by the player is made of 5 letters"""
    try:
        if word.isalpha() is False:
            raise ValueError(
                "All characters of the word must be alphabet letters"
            )
        if len(word) != 5:
            raise ValueError(
                "Word should consist of 5 letters"
            )

    except ValueError as e:
        print(colored(f"\nInvalid data: {e}.", "red")
              + colored("\nPlease try again. \n", "light_red"))
        return False

    return True


def check_word_in_library(word):
    """
    Check if the guessed word is in the word library.
    """
    with open("wordlibrary.txt") as f:
        word_library = f.read().splitlines()
        if word in word_library:
            return True
        else:
            print(colored("Word not found in the library. Try another word.",
                          "red"))
            return False


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


def game_play(word, level):
    """
    Function for game play:
    allows the user to start guessing the word withing an amount of attempts
    prints the guessed word with colored letters to signal correct letters
    and their positions Game ends when when word is guessed or number of
    allowed attempts is exceeded
    """

    # To determining the number of attempts based on the difficuty level chosen
    i = 0
    if level == "1":
        i = 7
        guess_list = ["-----", "-----", "-----", "-----", "-----", "-----"]
    else:
        i = 5
        guess_list = ["-----", "-----", "-----", "-----"]

    clear_terminal()
    print("Press 'q' to quit\n\n")
    print(fontstyle.apply(" ".rjust(33) + "Word Wander\n\n".ljust(30), 'bold/yellow'))
    print("Guess away creature\n\n")
    # print(word + "\n")

    for line in range(len(guess_list)):
        print(guess_list[line])

    for trial in range(1, i):

        while True:
            # So there won't be issues if the user types with capital letters
            guess = input("\n").lower()

            if guess == 'q':
                print("Goodbye!")
                exit()

            if validate_word(guess):
                if check_word_in_library(guess):
                    break

        guess_str = ""
        green_guess_str=""
        green_letters = 0
        # print colored letters
        for j in range(min(len(guess), 5)):
            if guess[j] == word[j]:

                green_guess_str += guess[j]
                green_letters += 1

            else: 
                green_guess_str += "-"


        for j in range(min(len(guess), 5)):
            if green_guess_str[j] == "-":

                if guess[j] in word and (guess_str.count(colored(guess[j], 'yellow')) + guess_str.count(colored(green_guess_str[j], 'green'))) == count_letter(word, guess[j]):

                    guess_str += guess[j]

                elif guess[j] in green_guess_str and guess.count(guess[j]) <= count_letter(word, guess[j]):
                    guess_str += colored(guess[j], 'yellow')

                elif guess[j] in green_guess_str and guess.count(guess[j]) > count_letter(word, guess[j]):
                    guess_str += guess[j]  

                elif guess[j] in word : # and (count_letter(word, guess[j]) <= guess.count(guess[j])):

                    guess_str += colored(guess[j], 'yellow')

                else:
                    guess_str += guess[j]
            else:
                guess_str += colored(green_guess_str[j], "green")

        guess_list[trial-1] = guess_str


        clear_terminal()
        print("Press 'q' to quit\n\n")
        print(fontstyle.apply(" ".rjust(33) + "Word Wander\n\n".ljust(30), 'bold/yellow'))
        print("Guess away creature!\n\n")

        for line in range(len(guess_list)):
            print(guess_list[line])

        if guess == word:
            print(colored("\nCongratulations! You guessed the word in "
                          "%i guesses!!" % trial, "green"))
            done = True
            break
        elif trial == i-1:
            print(colored(f"\nYou didn't guess the word within {i-1} "
                          "tries, it was '%s'." % word, "grey",
                          "on_light_red", ["bold"]))
            done = True
            break

    if done:

        while True:

            end_game = input(colored("\npress 'c' to play another game or "
                                     "'b' to go back to game menu.\t",
                                     "light_blue"))
            print()
            if end_game.lower() == 'q':
                print("Goodbye!")
                exit()

            if validate_entry("done", end_game):
                break

        if end_game.lower() == "c":
            start_new_game(level)
        else:
            main()


def start_new_game(level):
    word = read_random_word()
    game_play(word, level)


def main():
    data = game_intro()
    name = data[0]
    level = data[1]

    start_new_game(level)


def start_game_from_rules():
    name = enter_name()
    level = difficulty_level(name)

    start_new_game(level)


main()
