# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:18:02 2022

@author: Sabrina
"""

from persona import Persona

persona1=Persona('sabrina', 'colignon')
print(persona1.nombre)
print(persona1.apellido)

nombre=input("ingrese nombre de la persona: ")
apellido=input("ingrese apellido de la persona: ")
persona2=Persona(nombre, apellido)
print(persona2.nombre)
print(persona2.apellido)
