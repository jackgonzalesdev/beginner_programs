'''
Created on Sep 22, 2018

@author: jgonzales
'''

a = []

def is_prime(number):
    
    if number < 2:
        return False
    elif number == 2 :
        return False
    elif number > 2 and number % 2 == 0 :
        return False
    else:
        for i in range(3,number + 1):
            if number % i == 0:
                return False
    return True
            

def run():
    
    number = int(input('Enter a number: '))
    
    result = is_prime(number)
    
    if result is True:
        print("El {} es primo".format(number))
    else:
        print("TU numero no es primo.")
        
    
        
    
    
        
    

if __name__ == '__main__':
    run()
    