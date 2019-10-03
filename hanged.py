# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'machine',
    'car',
    'programmer',
    'python',
    'hello',
    'world',
    'computer',
    'keyboard',
    'music',
    'byte',
    'bit',
    'debbuging',
    'work',
    'elephant',
    'programming',
    'issue',
    'github'
]

def fill_all_letters(hidden_word, current_letter):
    for index in range(len(current_letter)):
        hidden_word[index] = current_letter[index]

def display_message(message):
    print('')
    print(message)

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Please introduce a charter or the complete word: '))

        letter_indexes = []

        if len( current_letter ) > 1:
            if current_letter == word:
                fill_all_letters(hidden_word, current_letter)
                display_board(hidden_word, tries)
                display_message('Congrats, you won!!. the word is: {}'.format(word))
                break
        else:
            for idx in range(len(word)):
                if word[idx] == current_letter:
                    letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                display_message('Sorry! :( the correct word is: {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            display_board(hidden_word, tries)
            display_message('Congrats, you won!!. the word is: {}'.format(word))
            break


if __name__ == '__main__':
    print('W E L C O M E')
    run()
