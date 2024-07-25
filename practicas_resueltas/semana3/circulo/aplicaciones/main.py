# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:39:52 2022

@author: Sabrina
"""

from circulo import Circulo

def main():
    
    calculado= False
    
    while not calculado:
    
        try:
            radio=int(input("ingrese valor del radio: "))
            c1 = Circulo(radio)
            
        except KeyError as msg:
            print(msg)
            
        except ValueError:
            print("ingrese valores numericos")
        
        else: 
            print(c1.radio)
            print("área del círculo:", c1.area)
            print("perímetro del círculo:", c1.perimetro)
        calculado=True
    
if __name__ == "__main__":
    
    main()