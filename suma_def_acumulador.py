'''
Created on Sep 17, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-


# *otros, este argumento se guardara en una tupla

def suma(a,b, *otros):
    acum = 0
    acum += a
    acum += b
    for o in otros:
        acum += o 
    return acum 
suma(1,1,2,3,4,5,8)
sum = suma()

print(type(sum))
 
    