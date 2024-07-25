# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:11:52 2022

@author: Sabrina
"""
from cuadrado_clase import Cuadrado

if __name__ == "__main__":
    cuadrado=Cuadrado(5)
    print(cuadrado.lado)
    
    cuadrado.lado=12
    print("area: ", cuadrado.area)
    print("perimetro: ", cuadrado.perimetro)