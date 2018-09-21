'''
Created on Sep 19, 2018

@author: jgonzales
'''

# -*- coding: utf-8 -*-

def factorial_imperativo(n):
    aux = 1
    for x in range(1, n + 1):
        aux *= x 
    return aux 

def factorial_funcional(n):
    if n == 0 :
        return 1
    else:
        return n * factorial_funcional(n-1)

if __name__ == '__main__':
    factorial = factorial_imperativo
    print(factorial(5))
    
    factorial = factorial_funcional
    print(factorial(5))