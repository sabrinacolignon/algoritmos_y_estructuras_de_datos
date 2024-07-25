# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:17:56 2022

@author: Sabrina
"""

# Implementar la clase Persona. Una persona posee un nombre y un apellido.
# La clase debe asegurarse que sus campos estén capitalizados y los mismos (campos o atributos)
# deben estar “ocultos”.


class Persona:
    def __init__(self, p_nombre, p_apellido):
        self._nombre=p_nombre
        self._apellido=p_apellido
    
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    
    @nombre.setter
    def nombre(self, p_nombre):
        self._nombre= self._nombre.capilatize()
    @apellido.setter
    def apellido(self, p_apellido):
        self._apellido= self._apellido.capilatize()