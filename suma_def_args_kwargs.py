'''
Created on Sep 18, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-

def suma(a=0, b=0, *args, **kwargs):
    print("args: ")
    print(args)
    print("kwargs: ")
    print(kwargs)
    aux = 0
    aux += a 
    aux += b 
    for v in args: 
        aux += v 
    for v in kwargs.values():
        aux += v 
        
    return aux

if __name__== '__main__':
    
    print(suma(1,1,1,1,1))
    print(suma(a=1, b=1, x=1, y=1, z=1))
    
    try:
        a = int(input("a: "))
    except ValueError:
        exit(1)

    try:
        b = int(input("b: "))
    except ValueError:
        exit(1)
        
    print(suma(a,b))