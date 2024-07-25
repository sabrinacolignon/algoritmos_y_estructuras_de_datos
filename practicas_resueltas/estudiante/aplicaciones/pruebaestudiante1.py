# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:15:20 2022

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
    
        
if __name__ == "__main__": 
       
    lista_estudiante=[]
    with open ("../datos/alumnos.txt", 'r') as archivo:
        contenido=archivo.readlines()
        for linea in contenido:
            linea=linea.rstrip("\n")
            linea=linea.split(",")
            legajo=linea[0]
            apellido=linea[1]
            nombre=linea[2]
            documento=linea[3]
            promedio=linea[4]
            estudiante= Estudiante(legajo, apellido, nombre, documento, promedio)   
            lista_estudiante.append(estudiante)
    
    for estudiante in lista_estudiante:
        print("Legajo: ", estudiante.legajo)
        print("Apellido: ", estudiante.apellido)
        print("Nombre: ", estudiante.nombre)
        print("Documento: ", estudiante.documento)
        print("Promedio: ", estudiante.promedio)