'''
Created on Sep 18, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-

MAXIMO = 100

def iterar(x):
    print(x)
    if x == MAXIMO:
        return 
    else:
        return iterar(x+1)
    
if __name__ == '__main__':
    iterar(1)