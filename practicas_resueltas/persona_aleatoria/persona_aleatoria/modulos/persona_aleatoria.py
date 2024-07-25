# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:04:41 2022

@author: Sabrina
"""
from persona import Persona

class PersonaAleatoria(Persona):
    def __init__(self, nombre, apellido):
        Persona.__init__(self, nombre, apellido)
        
    # @property
    # def crea_persona(self):
    #     with open ('./datos/datos.txt', 'r') as archivo:
    #         contenido=archivo.readlines()
    #         for linea in contenido:
    #             linea=linea.rstrip('\n')
    #             linea=linea.split(' ')
    #             self._nombre=linea[0]
    #             self._apellido=linea[1]
                
                