# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:28:49 2022

@author: Sabrina
"""

from estudiante import Estudiante

listado=[]
with open ("../datos/alumnos.txt", 'r') as archivo:
    contenido=archivo.readlines()
    for linea in contenido:
        linea=linea.rstrip('\n')
        linea=linea.split(',')
        documento=linea[0]
        apellido=linea[1]
        nombre=linea[2]
        legajo=linea[3]
        promedio=linea[4]
        alumno=Estudiante(documento, apellido, nombre, legajo, promedio)
        listado.append(alumno)
    
    
    for alumno in listado:
        print("legajo: ", alumno.legajo)
        print("apellido: ", alumno.apellido)
        print("nombre: ", alumno.nombre)
        print("docuemnto: ", alumno.documento)
        print("promedio: ", alumno.promedio)