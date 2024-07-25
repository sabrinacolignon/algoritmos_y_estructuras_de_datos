# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:02:47 2022

@author: Sabrina
"""

from modulos.circulo import Circulo

def main():
    circulo1= Circulo(5)
    print(circulo1.get_area())
    
if __name__== "__main__": #le da orden, se corre unicamente cuando se corre el archivo
    main()