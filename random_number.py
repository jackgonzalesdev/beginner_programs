'''
Created on Aug 16, 2018

@author: jgonzales
'''
import random
from getpass import _raw_input


numero = random.randrange(1,100)
respuesta = None

print ("Ud. debera adivinar un numero entre 1 y 100")

while respuesta != numero:
    print("Ingrese un numero entre 1 y 100")
    x = _raw_input()
    
    try:
        x =  int(x)
    except ValueError:
        print("Ud. no ha ingresado un numero entre 1 y 100")
        
    if x > numero:
        print("El numero es menor")
        
    elif x < numero:
        print("EL numero es mayor")
    
    else:
        print("Adivino! La respuesta era ")

