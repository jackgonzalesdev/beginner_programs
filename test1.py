'''
Created on Sep 28, 2018

@author: jgonzales
'''
word = str(input('escribe una letra: '))
letters = []

for letter in word: 
    letters.insert(0, letter)
    print(letters)
print(letters)

reversed_letter = ''.join(letters)
print(reversed_letter)