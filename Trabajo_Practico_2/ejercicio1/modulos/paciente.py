# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:35:29 2022

@author: Sabrina
"""

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    
    """Método inicializador de un paciente"""
    def __init__(self, turno : int):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__turno = turno 
        

    """Método para retornar el nombre del paciente"""
    @property
    def nombre(self):
        return self.__nombre
    
    """Método para retornar el apellido del paciente"""
    @property
    def apellido(self):
        return self.__apellido
    
    """Método para retornar el grado numérico de riesgo del paciente"""
    @property
    def riesgo(self):
        return self.__riesgo
    
    """Método para retornar la clasificación del grado de riesgo del paciente"""
    @property
    def descripcion_riesgo(self):
        return self.__descripcion
    
   
    """Método para retornar el número de turno"""
    @property
    def turno(self):
        return self.__turno
   
    
   
    """Método para mostrar los datos del paciente"""
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    
    """Método para comprar cuando un riesgo a menor a un riesgo b"""
    def __lt__ (self, otro ):
        if self.__riesgo == otro.__riesgo:
            return self.__turno < otro.__turno
        return self.__riesgo < otro.__riesgo
    
    
 
