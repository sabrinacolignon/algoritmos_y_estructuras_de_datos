# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:12:39 2022

@author: Sabrina
"""

from persona_aleatoria import PersonaAleatoria

lista=[]
with open ('../datos/datos.txt', 'r') as archivo:
    contenido=archivo.readlines()
    for linea in contenido:
        linea=linea.rstrip('\n')
        linea=linea.split(' ')
        nombre=linea[0]
        apellido=linea[1]
        persona=PersonaAleatoria(nombre, apellido)
        lista.append(persona)

for persona in lista:
    print("nombre: ", persona.nombre)
    print("apellido: ", persona.apellido)
                