# import words from words files
import random
from words import words

# Intro rules
print('\n')
print('Welcome to the Hangman game!\n')
print('@@@@@@@@@@@@@@@@')
print('@@@@@@@  @@@@@@@')
print('@@@@@@    @@@@@@')
print('@@@@@@@  @@@@@@@')
print('@@@          @@@')
print('@@@@@@@  @@@@@@@')
print('@@@@@@    @@@@@@')
print('@@@@@  @@  @@@@@')
print('@@@@@  @@  @@@@@')
print('@@@@   @@   @@@@')
print('@@@@@@@@@@@@@@@@')

print('\n')
print('Rules:')
print('You have 5 chances to guess the word,')
print('each time you guess wrong you lose a limb..on the')
print('last try its game over. Good luck and stay alive!\n')

# Get users name
def get_user():
    """
    Get users name for a more personalised game
    """
    user_name = input('Before we begin, can I take your name? \n')
    if user_name.isalpha():
        return user_name
    else:
        print("Letters only...try again")
        get_user()


# Store users name in variable
name = get_user()

# Get word from words.py file
def get_word():
    """
    Get a random word from word.py file for game play
    """
    word = random.choice(words)
    return word.upper()

# Play game using random word generated
def play(word):
    """
    Function to play the game
    """
    # Game variables
    lives = 5
    guessed_letters = []
    guessed_words = []
    guessed = False
    # Change chosen word for game
    full_word = '_' * len(word)
    print('\n')
    print(f'Your word is: {full_word}')
    # Game loop while user has lives left
    while not guessed and lives > 0:
        # Display game stats
        print('\n')
        print(f'You have {lives} chances left')
        if len(guessed_letters) >= 1:
            print('You have guessed letters:')
            print(', '.join(guessed_letters))
        if len(guessed_words) >= 1:
            print('You have guessed words:')
            print(', '.join(guessed_words))
        # Get users guess
        print('Input exit if you get scared...')
        guess = input('Choose a letter or word: \n').upper()
        print('\n')
        print('- - - - - - - - - - - - - - - - - - - - ')
        # Else/if statements if user chooses a letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('\n')
                print("You've already tried this letter!")
            elif guess not in word:
                lives -= 1
                guessed_letters.append(guess)
                if lives > 0:
                    print('\n')
                    print(f"Ouch {name}...you've lost a limb")
                else:
                    print('\n')
                    print(f'RIP {name}...the word was {word}')
                    rip()
            else:
                guessed_letters.append(guess)
                listed_word = list(full_word)
                checker = [i for i, letter in enumerate(word) if letter == guess]
                for index in checker:
                    listed_word[index] = guess
                full_word = "".join(listed_word)
                if "_" not in full_word:
                    guessed = True
                else:
                    print('\n')
                    print(f'Well done {name}...one step closer')
        # If user types exit
        elif guess == 'EXIT':
            print('\n')
            print('Scaredy pants...')
            ready_to_play()
            return
        # Else/if statements if user chooses a word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('\n')
                print('This word was incorrect the first time you tried it...')
            elif guess != word:
                lives -= 1
                guessed_words.append(guess)
                if lives > 0:
                    print('\n')
                    print(f'Nope, {guess} is wrong')
                else:
                    print('\n')
                    print(f'RIP {name}...the word was {word}')
                    rip()
            else:
                guessed = True
                full_word = word
        # Alternative input from user
        else:
            print('\n')
            print('To survive requires a valid input...')
        print('\n')
        print(f'Your word is: {full_word}')
        print(hangman(lives))

    # Direct user to win function if they guess correct
    if guessed:
        print('\n')
        print(f'Well done {name}, you survived!')
        win()

# Hangman lives
def hangman(lives):
    """
    Response images to show users lives
    """
    stages = [
        # Blank entry for the last life - replaced with win or lose image
        '',
        """
        @@@@@@@@@@@@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@
        """,
        # Missing both arms and right leg
        """
        @@@@@@@@@@@@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@  @@@@@@@@@
        @@@@@  @@@@@@@@@
        @@@@   @@@@@@@@@
        @@@@@@@@@@@@@@@@
        """,
        # Missing both arms
        """
        @@@@@@@@@@@@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@  @@  @@@@@
        @@@@@  @@  @@@@@
        @@@@   @@   @@@@
        @@@@@@@@@@@@@@@@
        """,
        # Missing right arm
        """
        @@@@@@@@@@@@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@@@  @@@@@@@
        @@@       @@@@@@
        @@@@@@@  @@@@@@@
        @@@@@@    @@@@@@
        @@@@@  @@  @@@@@
        @@@@@  @@  @@@@@
        @@@@   @@   @@@@
        @@@@@@@@@@@@@@@@
        """
    ]
    return stages[lives]


# Losing image
def rip():
    """
    RIP image for if a user loses the game
    """
    print('\n')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@       @@@@@@@   @@@@@@        @@@')
    print('@@   @@@   @@@@@   @@@@@@   @@@   @@')
    print('@@   @@@   @@@@@   @@@@@@   @@@   @@')
    print('@@   @@@   @@@@@   @@@@@@   @@@  @@@')
    print('@@   @   @@@@@@@   @@@@@@       @@@@')
    print('@@   @@   @@@@@@   @@@@@@   @@@@@@@@')
    print('@@   @@@   @@@@@   @@@@@@   @@@@@@@@')
    print('@@   @@@   @@@@@   @@@@@@   @@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\n')
    ready_to_play()

# Winning image
def win():
    """
    Smiling image for if a user wins the game
    """
    print('\n')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@               @@@@@@@@')
    print('@@@@@@  @@@@@@@@@@@@@@@  @@@@@@')
    print('@@@@  @@@@@@@@@@@@@@@@@@@  @@@@')
    print('@@  @@@@@@@@  @@@  @@@@@@@@  @@')
    print('@@  @@@@@@@@  @@@  @@@@@@@@  @@')
    print('@@  @@@@@@@@  @@@  @@@@@@@@  @@')
    print('@@  @@@@@@@@@@@@@@@@@@@@@@@  @@')
    print('@@  @@@@  @@@@@@@@@@@  @@@@  @@')
    print('@@  @@@@@@  @@@@@@@   @@@@@  @@')
    print('@@@@  @@@@            @@@@  @@@')
    print('@@@@@@  @@@@@@@@@@@@@@@@   @@@@')
    print('@@@@@@@@               @@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\n')
    ready_to_play()

# Loop to play game if user wants to continue
def ready_to_play():
    """
    Asks user if they would like to play, calls on function to start game if yes
    """
    print('\n')
    if input(f'So..{name} are you ready to play? (Y/N): ').upper() == 'Y':
        print('\n')
        print('- - - - - - - - - - - - - - - - - - - - ')
        word = get_word()
        play(word)
    else:
        print('\n')
        print("Ah, I see...come back when you're brave enough")

ready_to_play()
