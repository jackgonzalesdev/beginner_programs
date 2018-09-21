'''
Created on Sep 18, 2018

@author: jgonzales
'''
# -*- coding: utf-8 -*-


def mapear(lista, funcion):
    nueva_lista = []
    for valor in lista:
        nueva_lista.append(funcion(valor))
        
    return nueva_lista

def filtrar(lista, funcion):
    nueva_lista = []
    for valor in lista:
        if funcion(valor):
            nueva_lista.append(valor)
    return nueva_lista

def reducir(lista, funcion, valor_inicial=0):
    aux = valor_inicial
    for x in lista:
        aux = funcion(aux, x)
    return aux


if __name__ == '__main__':
    
    numeros = list(range(1,10 + 1))
    print(numeros)
    cuadrados = mapear(numeros, lambda x: x*x)
    print(cuadrados)
    
    cuadrados_pares = filtrar(cuadrados, lambda x: x%2==0)
    print(cuadrados_pares)
    
    print(reducir(cuadrados_pares, lambda x,y: x+y,0))
    