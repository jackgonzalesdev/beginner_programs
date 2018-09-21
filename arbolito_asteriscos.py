'''
Created on Aug 31, 2018

@author: jgonzales
'''

ASTERISCO_INICIAL = 1
ASTERISCO_FINAL = 15
VECES = 1 
NUMERO_ESPACIOS = 15

while VECES <= 32:
    print(" "*NUMERO_ESPACIOS, "*" * VECES)
    
    VECES += 2
    NUMERO_ESPACIOS -= 1
