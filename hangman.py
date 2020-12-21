import random



def load_words():
    words = []  # list of the words to read from the file
    with open('words.txt', 'r') as fp:
        for line in fp:  # iterate througth the file (line by line)
            words += line.split()  # split each line into words and append them to list
    return words


def get_secret_word(words, chances=10):
    ws = list(filter(lambda w : len(w) <= chances, words)) # pick up the words which length is less or equal to the number of chances offered to the player
    pos = random.randint(0, len(ws))  # get a random position
    return ws[pos]  # return a random word at the given position


def display_secret_word(secret_word, guessed_letters):
    display_letters = [c if c in guessed_letters else '_' for c in secret_word]  # iterate through the letters guessed by player and replace undiscovered ones by '_'
    print(' '.join(display_letters).upper())


def guess_word(secret_word, chances):
    letters = set(secret_word)  # get unique letters in the secret word
    guessed_letters = set()  # container of the letters well guessed by the player
    history = set()  # container of the player letters
    turn = 1  # variable to store the number of turns
    while turn <= chances:
        display_secret_word(secret_word, guessed_letters)  # display the current status of the word
        letter = input(f'Enter one letter ({turn}/{chances}): ').lower()
        if letter in history:
            print(f'You already played this letter ({letter}).')
        else:
            if letter in letters:  # check if the played letter is in the secret word
                guessed_letters.add(letter)  # register it
            if len(guessed_letters) == len(letters):  # check if all letters have been discovered
                return +1  # stop the loop with win status
            history.add(letter)  # register the played letter
            turn += 1  # increase the number of turn (decrease the chances)
    return -1  # reach the maximum number of tries


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
            print('You lost! The word to guess was:', secret_word.upper())
        play_again = input('\nDo you want to play again (y/n)? ').lower() == 'y' # asking the player for another party
    print('Goodbye!')
    
    
