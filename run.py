# import words from words files
import random
from words import words

# Intro rules
#print('Welcome to the Hangman game!\n')
#print('Rules:')
#print('you have 5 chances to guess the letters in the word,')
#print('each time you guess wrong you lose a limb..on the last try its game over.')
#print('Good luck and stay alive!\n')

# Get users name
def get_user():
    user_name = input('Before we begin, can I take your name? \n')
    return user_name

# get_user()

# game variables
lives = 5
guessed_letters = []
guessed_words = []

# Get word from list
def get_word():
    word = random.choice(words)
    return word.upper()

# Convert word 
def play(word):
    full_word = '_' * len(word)
    print('\n')
    print(f'Your word is: {full_word}')
    print('\n')

# Game statistics
def game_statistics():
    print(f'You have {lives} chances left')
    if len(guessed_letters) >= 1:
        print(f'You have guessed: {guessed_letters}')
    if len(guessed_words) >= 1:
        print(f'You have guessed: {guessed_words}')


def run_game():
    word = get_word()
    play(word)
    game_statistics()

run_game()
