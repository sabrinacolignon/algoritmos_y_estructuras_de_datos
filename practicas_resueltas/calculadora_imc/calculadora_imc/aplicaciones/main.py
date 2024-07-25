# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:48:02 2022

@author: Sabrina
"""

from calculadora import Calculadora

control=False

while not control:
    try:
        peso=int(input("ingrese peso en kg: "))
        altura=float(input("ingrese altura en m: "))
        persona=Calculadora(peso, altura)
    except KeyError as msg:
        print(msg)
    except ValueError:
        print("los valores deben ser mayor que cero")
    else:
        print(persona.calcula_imc)
        control=True
        
        