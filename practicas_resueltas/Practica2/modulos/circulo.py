# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:40:31 2022

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
        self._radio = radio
        
    def get_radio(self):
        """getter de radio"""
        return self._radio #es lo mismo que self.radio, lo que hace el guion bajo es que no acceda directamente
    
    def set_radio(self, valor):
        """setter de radio
        ----------
        valor : int
            valor entero positivo para modificar el radio.
        """
        self._radio = valor
        
    def get_area(self):
        """calcula y retorna el valor del área con 2 decimales de precisión"""
        area = math.pi*self.get_radio()**2
        return round(area, 2)
    
    def get_perimetro(self):
        """calcula y retorna el valor del perímetro con 2 decimales de precisión"""
        perimetro = 2*math.pi*self.get_radio()
        return round(perimetro, 2)        

#para realizar pruebas rapidas:
if __name__ == "__main__": 
    
    c1 = Circulo(5) #creo objeto circulo de radio 5

    print(c1.get_radio())
    print(c1._radio)
    
    print(c1.get_area())
    print(c1.get_perimetro())