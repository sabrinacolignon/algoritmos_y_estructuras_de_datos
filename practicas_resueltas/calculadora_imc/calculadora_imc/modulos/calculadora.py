# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:35:56 2022

@author: Sabrina
"""

class Calculadora:
    
    def __init__(self, p_peso, p_altura):
        self.peso=p_peso
        self.altura=p_altura
    
    @property
    def peso(self):
        return self._peso
    
    @property
    def altura(self):
        return self._altura
   
    @peso.setter
    def peso(self, p_peso):
        if p_peso<=0:
            raise ValueError("peso debe ser un numero")
        self._peso=p_peso
            
    @altura.setter
    def altura(self, p_altura):
        if p_altura<=0:
            raise KeyError("altura debe ser un numero")
        self._altura=p_altura
    
    @property
    def calcula_imc(self):
        imc=round(self.peso/(self.altura**2),2)
        condicion=0
        if imc<18.5:
            condicion= f" Tu IMC {imc} está debajo de lo normal"
        elif imc<25:
            condicion = f"Tu IMC {imc} es normal"
        elif imc<30:
            condicion= f"Tu IMC {imc} indica sobrepeso"
        else:
            condicion = f"Tu IMC {imc} indica Obesidad"
        return condicion