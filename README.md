# Word Wander

![Word Wanter title](/images/game-title.png)

Word Wander is a Python-based word guessing game inspired by the famous Wordle game. The game challenges players to guess a secret 5-letter word within a limited number of attempts. Players receive feedback after each guess to guide them towards the correct answer. Can you find the secret word and emerge as the ultimate Word Wanderer?

The live link can be found here - [Word Wander](https://word-wander-c212ee79ed5a.herokuapp.com/)


# Game flowchart:

...


# User Experience (UX)

Word Wander is a simple and engaging word guessing game inspired by the famous Wordle game. Below is an outline of the user experience:

1. Game Introduction:
   Upon launching the game, the user is welcomed and presented with two options: 
   - starting the game
   - Displaying the instructions
2. Guessing the Word:
   - The user tries to guess the secret 5-letter word.
   - After each guess, feedback is provided to indicate the correctness of the letters guessed:
     - Correct and in the right position: Highlighted in green.
     - Correct but in the wrong position: Highlighted in yellow.
     - Incorrect: Not highlighted.
   - The user continues guessing until they find the word or exceed the maximum allowed attempts.
3. Difficulty Levels:
   The game offers two difficulty levels, users can choose the difficulty level they prefer:
   - Easy (6 attempts)
   - Difficult (4 attempts)
4. Game Over:
   - The game ends when the word is guessed correctly or the user exceeds the maximum attempts allowed.
   - The user has the option to start a new round and guess a different secret word.
5. Command for Quitting:
   At any time, the user can quit the game by entering 'q'.


# How to play

   - The goal is to guess the secret word correctly within 4 or 6 attempts,
   depending on the chosen difficulty level.

   - To make a guess, type in a word of 5 letters and press enter.

   - Every guess must be a valid 5-letter word from the game's dictionary.

   - After each guess, a feedback is provided on the letters guessed:

     - Correct and in the right position: The letter is highlighted in green.
     - Correct and in the wrong position: The letter is highlighted in yellow.
     - Incorrect: The letter is not highlighted and isn't part of the secret word.

   -  You win if you guess the secret word within the allotted number of attempts, and lose if you fail to do so.

   - Once the game is over, you can start a new round and guess a different secret word.


# Existing Features

##  Main menu / Welcome page:

The game begins with a welcoming message to set the mood, creating an engaging atmosphere. It offers users two options: to start playing or to check the instructions.

![Welcome page](https://github.com/Ahmadk-g/WordWander/blob/main/images/game-title.png)

## Input validator:

Only accepts inputs that match the given options. If the input doesn't match, an error message gets displayed and ask of the user to try again.

![Error message](https://github.com/Ahmadk-g/WordWander/blob/main/images/error-message1.png)

## Game instructions:
The game includes an option for users to view the game instructions.
- After the user inputs the number 2, they are directed to the game instructions.


![Game instructions](https://github.com/Ahmadk-g/WordWander/blob/main/images/game-instructions.png)

## Step 1 of starting game

- The initial step of starting the game includes a text designed to immerse the user in the challenging mood of the game.
- Engages the user by asking for their name while maintaining the mood.

![Game question1](https://github.com/Ahmadk-g/WordWander/blob/main/images/game-start-q1.png)

## Step 2 of starting game

- During the second step of starting the game, the user selects their preferred difficulty level.
- This choice determines the number of attempts the user has to guess the word.
- "Simple mortal" for 6 trials and "Infinite Intellect" for 4 trials.


![Game question2](https://github.com/Ahmadk-g/WordWander/blob/main/images/game-start-q2.png)

## Game start

- The game begins with the phrase "guess away creature."
- Afterward, a series of dashed lines appear, the quantity determined by the chosen difficulty level. Beneath these lines, the player can enter their guesses.
- Beneath these lines, the player can enter their guesses.

![First guess](https://github.com/Ahmadk-g/WordWander/blob/main/images/first_guess.png)

## Guess till you win or lose

- If the player correctly guesses the word within the allotted number of attempts, they receive a congratulatory message.

![Win guess](https://github.com/Ahmadk-g/WordWander/blob/main/images/win-guess.png)

- If they fail to guess the word within the given attempts, they will discover what the word was.

![lose guess](https://github.com/Ahmadk-g/WordWander/blob/main/images/lose-guess.png)

As illustrated, in either scenario, players are prompted to play another game or return to the main menu. Quitting is always an option.

## Word guess validation

An important feature is validating the words entered for the guess.

- They must be acceptable 5-letter words that are found within the extensive word library file.
- They must consist solely of alphabetic characters.

An error message is displayed when the input doesn't pass validation.

![word not in library error](https://github.com/Ahmadk-g/WordWander/blob/main/images/not_word_err.png)

![not just letters error](https://github.com/Ahmadk-g/WordWander/blob/main/images/not_letters_err.png)


# Features to be implemented 

- Connect googlesheet for the integration of a scoring system.
- Implementing hints or clues for players.
- Enhancing error handling and validation process


# Technologies used


The script was implemented using __Python__.


- `VS Code`: Employed as the primary integrated development environment (IDE).
- `Git`: Employed for version control.
- `Github`: Utilized for file storage and hosting.
- `Heroku`: Utilized for hosting the deployed backend site.

__Modules imported for the script__

- `random` : Generates random numbers or selects random items from a sequence.
- `termcolor` : Provides functions for formatting text with ANSI color codes. 
- `sys` : Provides access to some variables used or maintained by the Python interpreter and functions that interact with the interpreter.
- `os` : Provides functions for interacting with the operating system, such as reading or writing files, manipulating paths, and executing system commands.
- `pyfiglet` : Generates ASCII art text from a string.
- `fontstyle` : Not a standard Python module; it may be a custom module for styling text.
- `time` : Provides various time-related functions.

