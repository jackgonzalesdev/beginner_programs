'''
Created on Sep 19, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-

from functools import reduce

if __name__ == '__main__':
    
    numeros = list(range(1,10 + 1))
    print(numeros)
    cuadrados = list(map(numeros, lambda x: x*x))
    print(cuadrados)
    
    cuadrados_pares = list(filter(cuadrados, lambda x: x%2==0))
    print(cuadrados_pares)
    
    print(reduce(cuadrados_pares, lambda x,y: x+y,0))