'''
Created on Sep 20, 2018

@author: jgonzales
'''
# -*- coding:utf-8 -*-

from random import randint

if __name__ == '__main__':
    
    coordenadas = []
    
    for i in range(10):
        latitud = (1 if randint(0,1) == 0 else -1) * randint(0,90)
        longitud = (1 if randint(0,1) == 0 else -1) * randint(0,180)
        
        punto = (latitud,longitud)
        coordenadas.append(punto)
        
    print(coordenadas)