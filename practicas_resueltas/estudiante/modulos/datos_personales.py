# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:31:36 2022

@author: Sabrina
"""

class Estudiante:
    
    def __init__(self, legajo, apellido, nombre, documento, promedio):
        self.legajo=legajo
        self.apellido=apellido
        self.nombre=nombre
        self.documento=documento
        self.promedio=promedio
     
    @property   #utilizar decoradores para getters y setters     
    def legajo(self): #getter de legajo
        return self._legajo
   
    @property   
    def apellido(self): #getter de apellido
        return self._apellido
    
    @property   
    def nombre(self): #getter de nombre
        return self._nombre
    
    @property   
    def documento(self): #getter de documento
        return self._documento
    
    @property   
    def promedio(self): #getter de promedio
        return self._promedio 
    
    @legajo.setter
    def legajo(self, legajo): #setter de legajo
        self._legajo=legajo
        
    @apellido.setter
    def apellido(self, apellido): #setter de apellido
        self._apellido=apellido
    
    @nombre.setter
    def nombre(self, nombre): #setter de nombre
        self._nombre=nombre
    
    @documento.setter
    def documento(self, documento): #setter de documento
        self._documento=documento
    
    @promedio.setter
    def promedio(self, promedio): #setter de promedio
        self._promedio=promedio
    
        
#if __name__ == "__main__": 
    
    #estudiante1= Estudiante(1234, "colignon", "sabrina", 41698150, 50) #creo objeto circulo de radio 5
   
    