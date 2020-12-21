import random


def load_words():
    words = []
    with open('words.txt', 'r') as fp:
        for line in fp:
            words += line.rstrip().split()
    return words


def get_secret_word(words, chances=10):
    ws = list(filter(lambda w : len(w) <= chances, words))
    pos = random.randint(0, len(ws))
    return ws[pos]


def display_secret_word(secret_word, guessed_letters):
    display_letters = ''
    for c in secret_word:
        if c in guessed_letters:
            display_letters += ' ' + c.upper() + ' '
        else:
            display_letters += ' _ '
    print(display_letters)


def guess_word(secret_word, chances):
    letters = set(secret_word)
    bag_of_letters = set()
    history = set()
    display_secret_word(secret_word, bag_of_letters)
    turn = 1
    game_end = 0
    while game_end == 0:
        letter = input(f'Enter one letter ({turn}/{chances}): ')
        if letter in history:
            print(f'You already played this letter ({letter}).')
        else:
            if letter in letters:
                bag_of_letters.add(letter)
            if len(bag_of_letters) == len(letters):
                game_end = 1
            elif turn == chances:
                game_end = -1
            history.add(letter)
            turn += 1
        display_secret_word(secret_word, bag_of_letters)
    return game_end


def welcome_message():
    print('**************************************************')
    print('**             Enjoy playing Hangman!           **')
    print('**************************************************')


if __name__ == "__main__":
    welcome_message()
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
    
    
