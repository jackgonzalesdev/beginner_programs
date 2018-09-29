'''
Created on Sep 29, 2018

@author: jgonzales
'''

# -*- coding: utf-8 -*-
import random

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =======''','''
    +---+
    |   |
    O   |
        |
        |
        |
        =======''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
        =======''','''
    +---+
    |   |
    O   |
  / |   |
        |
        |
        =======''','''
    +---+
    |   |
    O   |
  / | \ |
        |
        |
        =======''','''
        
    +---+
    |   |
    O   |
  / | \ |
    |   |
        |
        =======''','''
        
    +---+
    |   |
    O   |
  / | \ |
    |   |
   /    |
        =======''','''
        
    +---+
    |   |
    O   |
  / | \ |
    |   |
   / \  |
        ======='''
    ]

WORDS = ['washing machine',
         'dryer',
         'furniture',
         'government',
         'deputy',
         'democracy',
         'keyboard'
         ]

def random_word():
    idx = random.randint(0,len(WORDS) - 1)                              #We choose a word from WORDS randomly and returning the word accordingly its index
    return WORDS[idx]
def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * ---')
def run():                                                                  
    word = random_word()                                                #We call the random_word function and save into variable word
    hidden_word = ['-'] * len(word)                                     #We create a list called hidden_word where is filled with - multiplied for length of variable word.
    tries = 0                                                           #We initialize variable tries in 0
    
    while True:                                                         #We initialize a while loop
        display_board(hidden_word, tries)                               #Displaying always the IMAGE accordingly the tries.
        current_letter = str(input('Escoge una letra: '))               
        
        letter_indexes = []                                             #We create other list named letter_indexes where it'll be filled with matched words.
                                                                            
        for idx in range(len(word)):                                    
            if word[idx] == current_letter:
                letter_indexes.append(idx)
                #print(letter_indexes)
                
        if len(letter_indexes) == 0:
            tries += 1
            
            if tries == 7 :
                display_board(hidden_word, tries)
                print('')
                print('You lost! The correct word is {}'.format(word))
                break
        else: 
            for idx in letter_indexes:
                hidden_word[idx] = current_letter                           #Each time the hidden_word index is equal to current_letter, 
                #print(idx)                                                             # THE PLACE OF THE INDEX OF HIDDEN_WORD  WILL BE REPLACED WITH CURRENT_WORD
            letter_indexes = []                                             #And then letter_indexes will be emptied.

        try:
            hidden_word.index('-')                                          #If '-' is found in hidden_word the while loop continues again
        except ValueError:                                                  #But if not, it means that the user completed all word and won.
            print('')
            print('Congratulations! You won. The correct word is {}'.format(word))
            break                                                           #Finally the loop stops with the keyboard break.
             
if __name__ == '__main__':                  
    print('Welcome to Hanged Game')
    run()                                   #Execute the run function