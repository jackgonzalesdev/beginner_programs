'''
Created on Sep 17, 2018

@author: jgonzales
'''

print("Comienzo")
cuenta = 0
for i in range(1, 7):
    if i % 2 == 0:
        cuenta = cuenta + 1
print(f"Desde 1 hasta 5 hay {cuenta} múltiplos de 2")