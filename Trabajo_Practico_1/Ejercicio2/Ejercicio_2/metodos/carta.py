# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:40:19 2022

@author: Sabrina
"""
from __future__ import annotations
#importar la lista doblemente enlazada??

class Carta:
    def __init__(self, p_numero, p_palo):
         self._numero = p_numero #entero y letras
         self._palo = p_palo #figuritas
         self._estado = False #esta abajo la carta
        
        #sobrecarga mayor __gt__, menor __lt__, ==: __eq__ 
        
    @property
    def numero(self):
        return self._numero

    @property
    def palo(self):
        return self._palo

    def voltea(self):
        self._estado = not self._estado
    
    def __lt__(self, carta_rival: Carta): #la carta se compara con otra
        return self.numero < carta_rival.numero #si es true o false
    
    