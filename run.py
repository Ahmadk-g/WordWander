import random 
from termcolor import colored
import sys
import os

def game_intro():

    """
    Introducing the user to the game, get name, choice of difficulty level, 
    and display rules if asked.
    """
    
    print("Welcome to Word Wander!\n")
    print("Only one way forward: guess the word chosen by the elites.\n")

    player_name = input("By what name do you go, human?\n")
    
    if player_name.lower() == 'q':
            print("Goodbye!")
            exit()

    while True:
        open_rules = input(f"Now, {player_name}, Do you understand the rules? (y/n):\n")
        
        if open_rules.lower() == 'q':
            print("Goodbye!")
            exit()

        if validate_entry("rules", open_rules):
            break

    if open_rules == "n":
        game_rules()

    print(f"\nYou shall now be tested, {player_name}")

    print("Choose your difficulty level:\n")
    print("1. (Easy) Simple Mortal - 6 trials")
    print("2. (Difficult) Infinite Intellect - 4 trials")
    
    while True:
        difficulty_lvl = input("Which of those are you? (1/2):\n")
        
        if difficulty_lvl.lower() == 'q':
            print("Goodbye!")
            exit()
        
        if validate_entry("difficulty", difficulty_lvl):
            break
        
    return difficulty_lvl, player_name 


def game_rules():
    """
    Rules of the game thag will appear when called for.
    """
    
    print("\n. The goal is to guess the secret word correctly within 4 or 6 attempts, depending on the difficulty level you choose.")
    print(". You make a guess by typing in a word of 5 letters and pressing enter.")
    print(". All guesses must be valid words in the game's dictionary.")
    print(". After each guess, a feedback is provided on the letters guessed")
    print("\t- Correct and in the right position: The letter is highlighted in green")
    print("\t- Correct and in the wrong position: The letter is highlighted in yellow")
    print("\t- Incorrect: The letter is not highlighted and isn't part of the secret word.")
    print(". You win if you guess the secret word within the allotted number of attempts, and lose if you fail to do so.")
    print(". Once the game is over, you can start a new round and guess a different secret word.")


def validate_entry(type, input):
    """ 
    Raises ValueError if string value does not match the given choices. 
    """

    try: 

        if type == "rules":
            if input != "y" and input != "n":
                raise ValueError (
                    "Input value should be y/n"
                )
        elif type == "difficulty":
            if input != "1" and input != "2":
                raise ValueError (
                    "Input value should be 1/2"
                )
    
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n") 
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
        if word.isalpha() == False:
            raise ValueError (
                "All characters of the word must be alphabet letters"
            )
        if len(word) != 5:
            raise ValueError (
                "Word should consist of 5 letters"
            )

    except ValueError as e:
        
        print(f"Invalid data: {e}, please try again. \n") 
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
            print("Word not found in the library. Try another word.")
            return False
        
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

    
def game_play(word, level):
    """
    Function for game play:
    allows the user to start guessing the word withing an amount of attempts
    prints the guessed word with colored letters to signal correct letters and their positions
    Game ends when when word is guessed or number of allowed attempts is exceeded
    """
    
    #For determining the number of attempts based on the difficuty level chosen
    i = 0
    if level == "1":
        i = 7
    else:
        i = 5
     
    clear_terminal() 
       
    print("Guess away creature\n")
    print(word + "\n") 
    
    for line in range(1, i):
        print("-----")
        
    for trial in range(1, i):
        while True:
            guess = input().lower() # So there won't be issues if the user types with capital letters
            
            if guess == 'q':
                print("Goodbye!")
                exit()

            if validate_word(guess):
                if check_word_in_library(guess):
                    break
                
         
        
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')   
        
        
        
        # print colored letters
        for j in range(min(len(guess), 5)):
            if guess[j] == word[j]:
                print(colored(guess[j], 'green'), end="")
            # elif guess[j] in word:
            elif guess[j] in word and word.count(guess[j]) == guess.count(guess[j]):
                print(colored(guess[j], 'yellow'), end="")
            else:
                print(guess[j], end="")
        print()
        
        if guess == word:
            print("Congratulations! You guessed the word in %i guesses." %trial)
            break
        elif trial == i-1:
            print(f"You didn't guess the word within {i-1} tries, it was '%s'" %word)
    

def main():
    data = game_intro()
    level = data[0]
    name = data[1]
    word = read_random_word()
    game_play(word, level)
    
    



main()
