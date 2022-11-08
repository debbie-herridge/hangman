# import words from words files
import random
from words import words

# Intro rules
print('Welcome to the Hangman game!\n')
print('Rules:')
print('you have 5 chances to guess the letters in the word,')
print('each time you guess wrong you lose a limb..on the last try its game over.')
print('Good luck and stay alive!\n')

# Get users name
def get_user():
    user_name = input('Before we begin, can I take your name? \n')
    return user_name

name = get_user()

# Get word from list
def get_word():
    word = random.choice(words)
    return word.upper()

# Play game using random word generated 
def play(word):

    #game stats
    lives = 5
    guessed_letters = []
    guessed_words = []
    guessed = False

    while not guessed and lives > 0:
        #display word
        full_word = '_' * len(word)
        print('\n')
        print(f'Your word is: {full_word}')
        print('\n')

        #display game stats
        print(f'You have {lives} chances left')
        if len(guessed_letters) >= 1:
            print(f'You have guessed: {guessed_letters}')
        if len(guessed_words) >= 1:
            print(f'You have guessed: {guessed_words}')

        #get users guess
        guess = input('Choose a letter or word: ').upper()
        # else/if statements if user chooses a letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already tried this letter!")
            elif guess not in word:
                print(f"Oh dear {name}...you've lost a limb")
                lives -= 1
                guessed_letters.append(guess)
            else: 
                print(f'Well done {name}..one step closer to the word')
                guessed_letters.append(guess)
                listed_word = list(full_word)
                checker = [i for i, letter in enumerate(word) if letter == guess]
                for index in checker:
                    listed_word[index] = guess
                full_word = "".join(listed_word)
                if "_" not in full_word:
                    guessed = True
        # else/if statements if user chooses a word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('This word was incorrect the first time you tried it...')
            elif guess != word:
                print(f'Nope, {guess} is wrong')
                lives -= 1
                guessed_words.append(guess)
            else: 
                guessed = True
                full_word = word
        # alternative input from user
        else:
            print('To survive requires a valid input...')
    if guessed:
        print('\n')
        print(f'Well done {name}!')
        win()
    else:
        print('\n')
        print(f'RIP {name}...the word was {word}')
        rip()

def rip():
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@: :: :@@@@@@@: :@@@@@@: :: :@@@@@')
    print('@@: :@@@: :@@@@@: :@@@@@@: :@@@: :@@')
    print('@@: :@@@: :@@@@@: :@@@@@@: :@@@: :@@')
    print('@@: :@@@: :@@@@@: :@@@@@@: :@@@: :@@')
    print('@@: :@: :@@@::@@: :@@::@@: :: :@@@@@')
    print('@@: :@@: :@@@@@@: :@@@@@@: :@@@@@@@@')   
    print('@@: :@@@: :@@@@@: :@@@@@@: :@@@@@@@@')
    print('@@: :@@@: :@@@@@: :@@@@@@: :@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\n')
    ready_to_play()

def win():
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@: :: :: : :@@@@@@@@@@@')
    print('@@@@@@@@::@@@@@@@@@@@::@@@@@@@@@')
    print('@@@@@@::@@@@@@@@@@@@@@@::@@@@@@@')
    print('@@@@::@@@@@@::@@@::@@@@@@::@@@@@')
    print('@@@@::@@@@@@::@@@::@@@@@@::@@@@@')
    print('@@@@::@@@@@@::@@@::@@@@@@::@@@@@')
    print('@@@@::@@::@@@@@@@@@@@::@@::@@@@@')
    print('@@@@::@@@@::@@@@@@@::@@@@::@@@@@')
    print('@@@@@@::@@@:::::::::@@@@::@@@@@@')
    print('@@@@@@@@::@@@@@@@@@@@::@@@@@@@@@')
    print('@@@@@@@@@@: :: :: : :@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\n')
    ready_to_play()

def ready_to_play():
    if input('Ready to play? (Y/N): ').upper() == 'Y':
        word = get_word()
        play(word)

ready_to_play()