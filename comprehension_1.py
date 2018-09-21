'''
Created on Sep 20, 2018

@author: jgonzales
'''
# -*- coding:utf-8 -*-
numeros = list(range(1,10+1))

for n in numeros:
    
    if n % 2 == 0:
        
        print(n)
             
print(sum([x*x for x in numeros if x*x % 2 == 0]))
 
