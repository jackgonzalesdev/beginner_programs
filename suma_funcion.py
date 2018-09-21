'''
Created on Sep 17, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-

from getpass import _raw_input


a = 0

b = 0

def suma(a,b):
    
    a = int(_raw_input("Ingrese primer numero: "))
    b = int(_raw_input("Ingrese segundo numero: "))
    
    print (a + b)
    return a +b 
suma(a,b)

sum = suma(a,b)

print(type(sum))