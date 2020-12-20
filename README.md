# hangman
Python programming language
Final project

Kodjo Klouvi (kodjo@osekoo.com)

November 2020

# Goal
The goal of this project is to implement the class world game “Hangman”.
Hangman is a popular word game in which the computer chooses a secret word and the player attempts to guess the word one letter at a time. If a guessed letter appears in the word, all instances of it are revealed. If not, the player loses a chance. If the guesser figures out the secret word before he or she runs out of chances, he or she wins. If not, the player loses.

# Get started
Download and save the list of words (https://raw.githubusercontent.com/professeurr/hangman/main/words.txt ) as a text file (words.txt) on your computer. It will be used in the program.
Implementation steps
Loading words
Implement a function called load_words() loading words from the file words.txt and returns a list of words.

```(python)
def load_words():
   pass
```
example of output:

```
['about', 'account', 'across', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'almost', 'among', 'amount', 'amusement']
```

# Getting a secret word
Implement a function called get_secret_word() taking a list of words as an argument and returning a word from a random index. Use the Python random module to get a random number between 0 and number of words.
Example:

```
import random

def get_secret_word(words):
   index = random.randint(0, len(words)) # retrieve a random number between 0 and len(words)
   pass
```


Where the variable words represents a list of words.

# Displaying the secret word
Implement a function called display_secret_word() taking as arguments the secret word (word to guess) and the list of letters already guessed by the player (guessed_letters). For each letter in the secret word if it is already guessed by the player, it’s printed (disclosed) otherwise the computer hides it by printing a dash ( _ ).


```
def display_secret_word(secret_word, guessed_letters):
   pass
```


# Guessing the secret word
Implement a function called guess_word() taking as arguments the secret word and the number of chances.

```
def guess_word(secret_word, chances):
   pass
```


This is the main function in which the program loops (while loop) until the player figures out the secret word or runs out of chances.

At the beginning, the secret word is displayed to the player using the function display_secret_word(). Obviously, at this stage only dashes are displayed indicating to the player the number of potential letters to guess.

At each step of the loop, the player is asked to enter a single letter:
If he already played this letter, the computer might output “You already played this letter (THE_LETTER)”
if the letter is in the secret word, it’s add to guessed_letters list
evaluate if the players figures out the secret word (wins) or run out of chances 
decrease of the number of chances and print out the remaining chances
display the secret word (display_secret_word(secret_word, guessed_letters))
At the end:
display if the player wins or loses the party.
return +1 if the player wins the party or -1 if not.

# Testing the game
This is the main function to test your program. Just copy and past it at the end of your program file. It should work if you implement the functions requested in the sections above.

```
if __name__ == "__main__":
   words = load_words() # loading the words from words.txt file
   chances = 10 # number of chances offered to the player
   play_again = True # a flag telling is the game is over or not
   print(f'Guess the secret word in {chances} tries')
   while play_again:
       secret_word = get_secret_word(words) # pull the secret word
       status = guess_word(secret_word, chances) # ask the player to guess the secret word in while loop statement
       if status == 1: # the player figured out the secret word
           print('You won!')
       else: # -1 the player run out of chances
           print('You lost!')
       play_again = input('\nDo you want to play again (y/n)? ').lower() == 'y' # asking the player for another party
   print('Goodbye!')
```

# Deliverable
This project can be implemented in groups of 2 or 3 persons.

Implement the steps described above in one Python file named hangman.py.
Your program should be well-documented and readable (variables and functions names, comments, structure, etc.)

Send the Python file to kodjo@osekoo.com with the subject “M1 Finance - Dauphine - Hangman project”. Put in the mail body the names of the persons involved in the project.

To be submitted before: December 20, 2020


