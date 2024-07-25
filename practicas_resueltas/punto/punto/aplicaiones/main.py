# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:25:40 2022

@author: Sabrina
"""

from punto_x_y import Punto_x_y

punto1=Punto_x_y(2,4)
print(punto1.coordx)
print(punto1.coordy)

#SETTEO VALORES DE COORDENADAS
px=int(input("ingrese coordenadas del punto x: "))
py=int(input("ingrese coordenadas del punto y: "))

punto2=Punto_x_y(px, py)
print(punto2.coordx)
print(punto2.coordy)