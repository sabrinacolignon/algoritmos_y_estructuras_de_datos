# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 18:22:13 2022

@author: Sabrina
"""

# Implementar una clase que modele un producto. El producto debe tener como atributos: 
# nombre, precio, y número de unidades (cantidad). Debe contar con operaciones para establecer los
# valores de sus atributos al momento de instanciarlo, y para modificar y retornar el valor de dichos
# atributos. La clase debe contar con un método para aplicar un descuento al precio del producto a
# partir de un valor porcentual, implementar también una función para mostrar la información del
# producto por consola.

class Producto:
    
    def __init__(self, p_nombre, p_precio, p_cantidad):
        self._nombre=p_nombre
        self._precio=p_precio
        self._cantidad=p_cantidad
    
    @property
    def nombre(self):
        return self._nombre
    @property
    def precio(self):
        return self._precio
    @property
    def cantidad(self):
        return self._cantidad
    
    @nombre.setter
    def nombre(self, p_nombre):
        self._nombre=p_nombre
    @precio.setter
    def precio(self, p_precio):
        self._precio=p_precio
    @cantidad.setter
    def cantidad(self, p_cantidad):
        self._cantidad=p_cantidad    
    
    @property
    def calcular_descuento(self): #si le agrego 'valor' como parametro no anda
        descuento= (self._precio*20)/100 #anda
        #descuento= (self._precio*valor)/100 #NO anda
        return round(descuento,2)
        
    