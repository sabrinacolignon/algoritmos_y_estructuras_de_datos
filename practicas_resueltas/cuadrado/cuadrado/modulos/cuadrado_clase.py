# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:12:23 2022

@author: Sabrina
"""
# Implementar una clase que modele a un cuadrado. El único atributo que posee es su lado.
# Dotar de operaciones al Cuadrado para ingresar el lado, mostrarlo, calcular y mostrar el
# área, calcular y mostrar el perímetro.


class Cuadrado:
    def __init__(self, p_lado):
        self.lado=p_lado
        
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, p_lado):
        if p_lado<=0:
            print("el valor debe ser mayor a cero.")
        else:
            self._lado=p_lado
    
    @property
    def area(self):
        area=self.lado*self.lado
        return round (area,2)
    
    @property
    def perimetro(self):
        perimetro=self.lado+self.lado+self.lado+self.lado
        return perimetro