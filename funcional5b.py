'''
Created on Sep 20, 2018

@author: jgonzales
'''
# -*- coding:utf-8 -*-

from random import randint

if __name__ == '__main__':
    
    coordenadas = [((1 if randint(0,1) == 0 else -1) * randint(0,90), (1 if randint(0,1) == 0 else -1) * randint(0,180)) for x in range(10)]
    
  
        
    print(coordenadas)