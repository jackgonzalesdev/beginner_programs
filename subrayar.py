'''
Created on Sep 18, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-

def subrayar(cadena, caracter='=', nl = False):
    print(cadena)
    print(caracter*len(cadena))
    if nl:
        print()
#subrayar("Hello World")
#subrayar("Hello World", "*")
subrayar("Hello World", "-", True)


