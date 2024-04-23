import random 
from termcolor import colored
import sys
import os
import pyfiglet

def title_ascii():
    """
    ascii art for game title
    """
    title_text_ascii = "Word Wander"
    word_wander_ascci_art = pyfiglet.figlet_format(
        title_text_ascii, font='epic', justify='center'
    )
    print(word_wander_ascci_art)


def game_intro():

    """
    Introducing the user to the game, get name, choice of difficulty level, 
    and display rules if asked.
    """
    clear_terminal()
    # print("\n\tWORD WANDER")
    title_ascii()
    print("\t___a wordle game___\n")
    
    print("1. Start playing")
    print("2. Check out the Rules")
    print("\n'q' to Quit\n")
    
    
    
    while True:
        menu_choice = input("For what do you wish?\n")
        
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
    print("Welcome to Word Wander!\n")
    print("Only one way forward: guess the word chosen by the elites.\n")
    
    
    player_name = input("By what name do you go, human?\n")
    
    if player_name.lower() == 'q':
            print("Goodbye!")
            exit()
    
    return player_name
    

def difficulty_level(player_name):
    """To allow the user to choose the difficulty of the game and return the value"""
    clear_terminal()
    print("Press 'q' to quit\n\n")
    print("Choose your difficulty level:\n")
    print("1. (Easy) Simple Mortal - 6 trials")
    print("2. (Difficult) Infinite Intellect - 4 trials")
    print()
    
    while True:
        difficulty_lvl = input("Which of those are you? (1/2):\n")
        
        if difficulty_lvl.lower() == 'q':
            print("Goodbye!")
            exit()
        
        if validate_entry("difficulty", difficulty_lvl):
            break
        
    print(f"\nYou shall now be tested, {player_name}")
    
    return difficulty_lvl

def game_rules():
    """
    Rules of the game thag will appear when called for.
    """
    clear_terminal()
    print("Press 'q' to quit\n\n")
    print("\tWORD WANDER\n")
    
    print("\n\t. The goal is to guess the secret word correctly within 4 or 6 attempts, depending on the chosen difficulty level.")
    print("\t. To make a guess, type in a word of 5 letters and press enter.")
    print("\t. Every guess must be a valid 5-letter word from the game's dictionary.")
    print("\t. After each guess, a feedback is provided on the letters guessed:")
    print("\t\t- Correct and in the right position: The letter is highlighted in " + colored("green", 'green'))
    print("\t\t- Correct and in the wrong position: The letter is highlighted in " + colored("yellow", 'yellow'))
    print("\t\t- Incorrect: The letter is not highlighted and isn't part of the secret word.")
    print("\t. You win if you guess the secret word within the allotted number of attempts, and lose if you fail to do so.")
    print("\t. Once the game is over, you can start a new round and guess a different secret word.\n")
    
    
    while True:
        rule_page_button = input("Press 'b' to go back to game menu and 'c' to start.\n")
        
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
                raise ValueError (
                    "Input value should be 1/2... or 'q' to quit"
                )
        
        elif type == "rules":
            if input.lower() != "b" and input.lower() != "c":
                raise ValueError (
                    "Input value should be b/q"
                )
        elif type == "difficulty":
            if input != "1" and input != "2":
                raise ValueError (
                    "Input value should be 1/2"
                )
        elif type == "done":
            if input.lower() != "c" and input.lower() != "b":
                raise ValueError (
                    "Input value should be c/b"
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
        guess_list=["-----","-----","-----","-----","-----","-----"]
    else:
        i = 5
        guess_list=["-----","-----","-----","-----"]
            
     
    clear_terminal() 
    print("Press 'q' to quit\n\n")
      
    print("Guess away creature\n")
    print(word + "\n") 
    
    for line in range(len(guess_list)):
        print(guess_list[line])
        
    for trial in range(1, i):
        
        while True:
            guess = input().lower() # So there won't be issues if the user types with capital letters
            
            if guess == 'q':
                print("Goodbye!")
                exit()

            if validate_word(guess):
                if check_word_in_library(guess):
                    break
                
        
        # sys.stdout.write('\x1b[1A')
        # sys.stdout.write('\x1b[2K')   
        
        guess_str = ""
        
        # print colored letters
        for j in range(min(len(guess), 5)):
            if guess[j] == word[j]:
                # print(colored(guess[j], 'green'), end="")
                guess_str += colored(guess[j], 'green')
            # elif guess[j] in word:
            elif guess[j] in word and word.count(guess[j]) == guess.count(guess[j]):
                # print(colored(guess[j], 'yellow'), end="")
                guess_str += colored(guess[j], 'yellow')
            else:
                # print(guess[j], end="")
                guess_str+= guess[j]
        # print()
        guess_list[trial-1]=guess_str
        
        clear_terminal()
        print("Press 'q' to quit\n\n")
        print("Guess away creature!\n")
        print(word + "\n")
        
        for line in range(len(guess_list)):
            print(guess_list[line])
        
        if guess == word:
            print("Congratulations! You guessed the word in %i guesses." %trial)
            done = True
            break
        elif trial == i-1:
            print(f"You didn't guess the word within {i-1} tries, it was '%s'" %word)
            done = True
            break    
    if done:
        
        while True:
            
           end_game = input ("press 'c' to play another game or 'b' to go back to game menu")
           
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
