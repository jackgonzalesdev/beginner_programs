'''
Created on Sep 20, 2018

@author: jgonzales
'''
# -*- coding:utf-8 -*-

a = 10

def imprimir_a():
    global a 
    a = 20 #Esto opaca a la variable global a = 10, por eso hay que llamar a la variable con la palabra global
    print(a)
    
if __name__ == '__main__':
    imprimir_a()
    print(a)