# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:22:58 2022

@author: Sabrina
"""

import math

class Circulo:
    """clase que modela un círculo mediante su atributo radio posee métodos para 
    modificar/obtener el radio y para calcular y devolver su perímetro y su área.
    -----------
    atributos:
        radio: int. valor entero que representa el radio del círculo
    """    
    def __init__(self, radio=0): #metodos magicos porque tiene doble guion bajo-> constructor      
        self.radio = radio
        
    @property   #utilizar decoradores para getters y setters     
    def radio(self):
        """getter de radio"""
        return self._radio #es lo mismo que self.radio, lo que hace el guion bajo es que no acceda directamente
   
    @radio.setter
    def radio(self, valor):
        """setter de radio
        ----------
        valor : int
            valor entero positivo para modificar el radio.
        """
        if valor>=0:
            self._radio = valor
        else:
            self._radio = 0
            print("El valor del radio no puede ser negativo")
    
    @property
    def area(self):
        """calcula y retorna el valor del área con 2 decimales de precisión"""
        area = math.pi*self.radio**2
        return round(area, 2)
    
    @property
    def perimetro(self):
        """calcula y retorna el valor del perímetro con 2 decimales de precisión"""
        perimetro = 2*math.pi*self.radio
        return round(perimetro, 2)        
    
        
if __name__ == "__main__": 
    
    circulo1 = Circulo(5) #creo objeto circulo de radio 5
    print("radio: ", circulo1.radio)
    circulo1.radio=4
    print("radio: ", circulo1.radio)
    print("area: ", circulo1.area)
    