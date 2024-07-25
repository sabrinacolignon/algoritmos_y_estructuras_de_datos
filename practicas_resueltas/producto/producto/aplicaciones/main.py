# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:22:07 2022

@author: Sabrina
"""

from producto import Producto


#porcentaje=float(input("Ingrese porcentaje de descuento: "))

producto1=Producto("fibra", 5, 10)

print(producto1.nombre)
print(producto1.precio)
print(producto1.cantidad)
print(producto1.calcular_descuento) #anda
#print(producto1.calcular_descuento(20)) # NO anda
#TypeError: descuento() missing 1 required positional argument: 'valor'

# nombre=input("Ingrese nombre del producto: ")
# precio=int(input("Ingrese precio del producto: "))
# cantidad=int(input("Ingrese cantidad de unidades disponibles: "))
# producto2=Producto(nombre, precio, cantidad)



