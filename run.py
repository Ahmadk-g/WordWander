# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def game_intro():
    print("Welcome to Word Wander!\n")
    print("Only one way forward: guess the word chosen by the elites.\n")

    player_name = input("By what name do you go, human?\n")

    open_rules = input(f"Now, {player_name}, Do you understand the rules? (y/n): ")

    if open_rules == "n":
        game_rules()

    print(f"\nYou shall now be tested, {player_name}")


def game_rules():

    print("\n. The goal is to guess the secret word correctly within 4 or 6 attempts, depending on the difficulty level you choose.")
    print(". You make a guess by typing in a word of the correct length and pressing enter.")
    print(". All guesses must be valid words in the game's dictionary.")
    print(". After each guess, a feedback is provided on the letters guessed")
    print("\t- Correct and in the right position: The letter is highlighted in green")
    print("\t- Correct and in the wrong position: The letter is highlighted in yellow")
    print("\t- Incorrect: The letter is not highlighted and isn't part of the secret word.")
    print(". You win if you guess the secret word within the allotted number of attempts, and lose if you fail to do so.")
    print(". Once the game is over, you can start a new round and guess a different secret word.")


game_intro()