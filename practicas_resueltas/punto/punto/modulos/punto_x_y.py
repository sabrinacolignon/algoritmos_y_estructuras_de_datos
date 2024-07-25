# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:26:02 2022

@author: Sabrina
"""

# Implementar una clase que modele un punto compuesto por dos coordenadas ‘x’ y ‘y’.
# El punto debe contar con operaciones para: proporcionar un valor al punto al momento
# de instanciarlo, proporcionar valores a sus atributos y para retornarlos.

class Punto_x_y:
    
    def __init__(self, p_x, p_y):
        self.coordx=p_x
        self.coordy=p_y
      
    @property
    def coordx(self):
        return self._coordx
    
    @property
    def coordy(self):
        return self._coordy
   
    @coordx.setter
    def coordx(self, p_x):
        if p_x<=0:
            raise ValueError("px debe ser un numero")
        self._coordx=p_x
            
    @coordy.setter
    def coordy(self, p_y):
        if p_y<=0:
            raise ValueError("pya debe ser un numero")
        self._coordy=p_y