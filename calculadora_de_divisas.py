'''
Created on Sep 21, 2018

@author: jgonzales
'''
# -*- coding:utf-8 -*-

def foreign_exchange_calculator(cantidad):
    soles = 3.25
    
    return soles*cantidad


def run():
    print("B A D G E S C A L C U L A T O R")
    print('Convert american dollar to soles')
    
    ammount = float(input('Enter the ammount in dollars: '))
    
    result = foreign_exchange_calculator(ammount)
    
    print('${} dollars is equal to {} soles'.format(ammount,result))
    print(" Thank you ")
if __name__ == '__main__':
    
    run()  