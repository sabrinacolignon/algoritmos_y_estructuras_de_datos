# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:57:27 2022

@author: Sabrina
"""

class Nodo:
    def __init__(self, p_dato_inicial):
        self.dato = p_dato_inicial
        self.siguiente = None
    
    @property
    def dato(self):
        return self.dato
    @dato.setter
    def dato(self, p_dato):
        self._dato=p_dato
    
    @property
    def siguiente(self):
        return self.siguiente
    @siguiente.setter
    def siguiente(self, p_siguiente):
        self._siguiente=p_siguiente
    
    @property
    def anterior(self):
        return self.anterior
    @anterior.setter
    def anterior(self, p_anterior):
        self._anterior=p_anterior