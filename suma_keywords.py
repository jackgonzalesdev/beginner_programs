'''
Created on Sep 18, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-

def suma(a,b, **otros):
    aux = 0
    aux += a
    aux += b 
    for v in otros.values():
        aux += v 
        
    return aux

print(suma(b=2, x=3, y=5, a=10))