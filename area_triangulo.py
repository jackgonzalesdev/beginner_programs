'''
Created on Aug 29, 2018

@author: jgonzales
'''

print("Area del Triangulo")
print("==================")
print("==================")

try:
    base = float(input("Ingrese la base: "))
except ValueError:
    print("La base tiene que ser un numero flotante.")
    exit(1)
try:    
    altura = float(input("Ingrese la altura"))
except ValueError:
    print("La altura tiene que ser un numero flotante.")
    exit(1)
area = (base * altura) / 2

print("Base: %.2f" %base)
print("Altura: %.2f" %altura)
print("Area: %.2f" %area)