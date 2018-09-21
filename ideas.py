'''
Created on Sep 20, 2018

@author: jgonzales
'''
# -*- coding:utf-8 -*-

def print_name():
    user = str(input("Ingrese su nombre porfavor: "))
    
    print("Hola", user)
    
    print_edad()


def print_edad():
    age = int(input("Ingrese su edad, porfavor: "))
    
    print(age)
    
    
    
if __name__ == "__main__":
    
    print_name()