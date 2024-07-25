
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 08:25:23 2022

@author: Mica
"""
from modulos.monticulo_max import ColaDePrioridadmax
from modulos.monticulo_min import ColaDePrioridad
import numpy as np


def dijkstra_peso(grafo,inicio): #inicio es un vertice
    ''' Esta función modifica el grafo que recibe para que sea un grafo que contenga 
        los valores MAXIMOS de los MINIMOS
    Parameters: -grafo: grafo
                -inicio: vértice    
    Returns: None.'''
    
    #encuentro el que me restringe menos
    #uso cola de prioridad de maximos para que me quede el maximo arriba
    #Utilizamos la distancia como valor para la cola de prioridad
    
    cp = ColaDePrioridadmax() #cola de prioridad->monticulo de maximos
    inicio.dist=np.Inf #DISTANCIA VERTICE INICIO= infinito, para que el costo minimo sea maximo
    #dist: maxima carga que puede llegar a ese nodo por algun camino

    cp.construir_monticulo([(v.dist, v) for v in grafo]) #construyo monticulo con todos los vertices del grafo
    
    while not cp.esta_vacia():
        verticeActual = cp.eliminar_max() 
        #modifica el grafo y solo quedan las conexiones del maximo de minimos
        
        for verticeSiguiente in verticeActual.obtener_conexiones(): 
            nuevaDistancia = min (verticeActual.dist, verticeActual.obtener_ponderacion(verticeSiguiente))
            #encuentro las nuevas distancias calculando los minimos
                        
            #BUSCA EL MAXIMO DEL MINIMO CALCULADO
            if nuevaDistancia > verticeSiguiente.dist: #verticeSiguiente.dist: originalmente cero
                verticeSiguiente.dist= nuevaDistancia #hallo el mayor de los menores
                verticeSiguiente.asignar_predecesor(verticeActual)                 
                cp.decrementar_clave(verticeSiguiente,nuevaDistancia) #ES NUEVO EN EL MONTÍCULO
                

def dijkstra_precio(grafo,inicio):
    '''Parameters:  -grafo: TYPE: grafo
                    -inicio: Vértice desde el que comienza a recorrer el grafo. TYPE: vertice. 
       Returns: None. '''
  
    cp = ColaDePrioridad() #cola de prioridad->monticulo de minimos
    for v in grafo:
        v.dist=np.Inf   #todos los otros estan en infinito
    
    inicio.dist= 0 #inicializo su distancia en cero
    
    cp.construir_monticulo([(v.dist,v) for v in grafo])
    
    while not cp.esta_vacia():
        verticeActual = cp.eliminar_min() #elimino el minimo
        
        for verticeSiguiente in verticeActual.obtener_conexiones():
            nuevoprecio = verticeActual.dist + verticeActual.obtener_ponderacion(verticeSiguiente)
            #nuevo precio es la suma de los costos de ir por x camino
            
            if nuevoprecio < verticeSiguiente.dist: #busca la menor de las sumas
                verticeSiguiente.dist= nuevoprecio
                verticeSiguiente.asignar_predecesor(verticeActual)
                cp.decrementar_clave(verticeSiguiente,nuevoprecio)