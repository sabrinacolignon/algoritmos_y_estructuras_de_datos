# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:29:17 2022

@author: Sabrina
"""

class Estudiante:
    def __init__ (self, p_nombre, p_apellido, p_documento, p_legajo, p_promedio):
        self._documento=p_documento
        self._apellido=p_apellido
        self._nombre=p_nombre
        self._legajo=p_legajo
        self._promedio=p_promedio
        
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def documento(self):
        return self._documento
    @property
    def legajo(self):
        return self._legajo
    @property
    def promedio(self):
        return self._promedio
    
    