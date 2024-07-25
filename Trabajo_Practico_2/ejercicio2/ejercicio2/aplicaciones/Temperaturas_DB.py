# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:44:22 2022

@author: Colignon Sabrina
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:28:06 2022

@author: Sabrina Colignon
"""
from AVL import AVL
from AVL import Iterador
from datetime import datetime


class Temperaturas_DB:
    
    """Método para inicializar la base de datos de temperatura
       internamente funciona como un arbol AVL"""
    def __init__(self):
        self.mediciones = AVL() 
        
    """Método que crea y guarda un nodo con clave en formato fecha y carga útil en formato temperatura
       la fecha se ingresa como string y se convierte a formato datetime"""
    def guardar_temperatura(self, p_fecha, p_temperatura): 
        fecha_dt = datetime.strptime(p_fecha, '%d/%m/%Y')
        
        self.mediciones.agregar(fecha_dt, p_temperatura)
        
    """Método que retorna el valor de la temperatura (carga útil) cuando recibe una fecha (clave).
       la fecha se ingresa como string y se convierte a formato datetime"""
    def devolver_temperatura(self, p_fecha):
        fecha_dt = datetime.strptime(p_fecha, '%d/%m/%Y')
        return self.mediciones.obtener(fecha_dt)

    """Método que encuentra y retorna el valor máximo de la temperatura en un rango de fechas: fecha1 y fecha2 inclusive (fecha1 < fecha2).
       la fecha se ingresa como string y se convierte a formato datetime"""
    def max_temp_rango(self, p_fecha1, p_fecha2):
        fecha1_dt = datetime.strptime(p_fecha1, '%d/%m/%Y')
        fecha2_dt = datetime.strptime(p_fecha2, '%d/%m/%Y')
 
        t_max=self.mediciones.obtener(fecha1_dt)
        
        iterador = Iterador(self.mediciones, fecha1_dt) #-> O(log(n)) por el _obtener
        
        for nodo in iterador: # O(n)

            if  fecha1_dt < nodo.clave <= fecha2_dt:
                if nodo.carga_util > t_max:
                    t_max = nodo.carga_util
        #como me quedo simepre con la peor el O de complejidad del método entero es o(n)
        return t_max
    
    """Método que encuentra y retorna el valor mínimo de la temperatura en un rango de fechas: fecha1 y fecha2 inclusive (fecha1 < fecha2).
       la fecha se ingresa como string y se convierte a formato datetime"""
    def min_temp_rango(self, p_fecha1, p_fecha2):
        fecha1_dt = datetime.strptime(p_fecha1, '%d/%m/%Y')
        fecha2_dt = datetime.strptime(p_fecha2, '%d/%m/%Y')
        
        t_min=self.mediciones.obtener(fecha1_dt)
        
        iterador = Iterador(self.mediciones, fecha1_dt)
        
        for nodo in iterador:

            if  fecha1_dt < nodo.clave <= fecha2_dt:
                if nodo.carga_util < t_min:
                    t_min = nodo.carga_util
                    
        return t_min
    
    """Método que encuentra y retorna una tupla de valores con la temperatura mínima y máxima en un rango de fechas: fecha1 y fecha2 inclusive (fecha1 < fecha2)."""
    def temp_extremos_rango(self, p_fecha1, p_fecha2):
        t_max = self.max_temp_rango(p_fecha1, p_fecha2)
        t_min = self.min_temp_rango(p_fecha1, p_fecha2)

        return t_min, t_max
    
    """Método que elimina la temperatura de un nodo recibiendo como parámetro la fecha
       la fecha se ingresa como string y se convierte a formato datetime"""
    def borrar_temperatura(self, p_fecha):
        fecha_dt = datetime.strptime(p_fecha, '%d/%m/%Y')
        self.mediciones.eliminar(fecha_dt)
    
    """Método que muestra las temperaturas guardadas en un rango de fechas.
       la fecha se ingresa como string y se convierte a formato datetime"""
    def mostrar_temperaturas(self, p_fecha1, p_fecha2):
        fecha1_dt = datetime.strptime(p_fecha1, '%d/%m/%Y')
        fecha2_dt = datetime.strptime(p_fecha2, '%d/%m/%Y')
        
        iterador = Iterador(self.mediciones, fecha1_dt)
        listado=[]
        
        for nodo in iterador:
            if  fecha1_dt <= nodo.clave <= fecha2_dt:
                fecha = nodo.clave.date()
                fecha_c = str(fecha.strftime('%d/%m/%Y'))
                carga = str(nodo.carga_util)+ "°C"
                listado.append(fecha_c+": " + carga)
        # return listado
        print(listado) #muestra por consola un listado de las mediciones
        
    """Método que retorna el valor total de registros"""
    def mostrar_cantidad_muestras(self):
        return self.mediciones.tamanio
    
