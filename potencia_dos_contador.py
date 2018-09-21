'''
Created on Aug 31, 2018

@author: jgonzales
'''

base =  2
potencia = 0
NUMERO_VECES = 5

while potencia <= NUMERO_VECES:
    print("Resultado de {} a la {} es: ".format(base, potencia),2**potencia)
    potencia += 1