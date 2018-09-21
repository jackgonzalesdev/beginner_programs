'''
Created on Sep 19, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-

from functools import reduce

if __name__ == '__main__':
    
    cadena = "Hola Mundo"
    letras = list(map(lambda letra: letra.upper(), cadena))
    print(letras)
    print(reduce(lambda a,b: ''.join([a,b]), letras, ""))
    
    