import random 

def game_intro():

    """
    Introducing the user to the game, get name, choice of difficulty level, 
    and display rules if asked.
    """
    
    print("Welcome to Word Wander!\n")
    print("Only one way forward: guess the word chosen by the elites.\n")

    player_name = input("By what name do you go, human?\n")

    while True:
        open_rules = input(f"Now, {player_name}, Do you understand the rules? (y/n): ")
        print(type(open_rules))

        if validate_entry("rules", open_rules):
            break

    if open_rules == "n":
        game_rules()

    print(f"\nYou shall now be tested, {player_name}")

    print("Choose your difficulty level:\n")
    print("1. (Easy) Simple Mortal")
    print("2. (Difficult) Infinite Intellect")
    
    while True:
        difficulty_lvl = input("Which of those are you? (1/2): ")
        if validate_entry("difficulty", difficulty_lvl):
            break


def game_rules():
    """
    Rules of the game thag will appear when called for.
    """
    
    print("\n. The goal is to guess the secret word correctly within 4 or 6 attempts, depending on the difficulty level you choose.")
    print(". You make a guess by typing in a word of the correct length and pressing enter.")
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

# game_intro()
read_random_word()