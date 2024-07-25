# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:50:34 2022

@author: Mica
"""

from modulos.algoritmos import dijkstra_peso, dijkstra_precio
from modulos.grafo import Grafo

                
def cuello_botella(grafo, desde, hasta):
    #cuello de botella: el valor maximo(peso) de los minimos de cada camino
    #porque pide el mayor peso en kg que se puede transporar: uso dijktra
    #tenemos un grafo ponderado y dirigido
    ''' Parameters: -grafo: TYPE: grafo, recibe el grafo en el que se busca el cuello de botella
                    -desde: vertice
                    -hasta: vertice
    Returns: devuelve el valor máximo entre los mínimos '''
    
    dijkstra_peso(grafo, grafo.obtener_vertice(desde))#LO CALCULA CON EL DEJKSTRA DE PESOS
    return grafo.obtener_vertice(hasta).dist #devuelve un valor int que es el peso

def minimo_precio (grafo, desde, hasta):
    ''' Parameters: -grafo: grafo, recibe el grafo en el que queremos buscar el costo mínimo 
                    -desde: vertice
                    -hasta: TYPE: vertice
    Returns: devuelve la suma de las ponderaciones de las aristas de la ruta más corta '''
  
    dijkstra_precio(grafo, grafo.obtener_vertice(desde))
    return grafo.obtener_vertice(hasta).dist
    
def transportar_por (grafo_pesos, desde, hasta):
    ''' Parameters: -grafo_pesos: grafo
                    -desde: vertice a partir del cual se comienza a recorrer el grafo 
                    -hasta: vertice al cuál llega el recorrido
        Returns: -cuello: el máximo cuello de botella del grafo que recibe
                 -menor_precio: el mínimo precio (suma de las aristas)'''
    
    cuello = cuello_botella (grafo_pesos, desde, hasta)
    
    grafo_precio = Grafo() #subgrafo del grafo pesos pero que ha sido filtrado por el cuello botella
    with open("../rutas.txt") as archivo:
        for linea in archivo:
            primerlinea= linea.rstrip().split(',')
            if int(primerlinea[2])>=cuello: #si el peso es mayor o igual al del cuello lo dejo pasar
                grafo_precio.agregar_arista(primerlinea[0], primerlinea[1], int(primerlinea[3]))
                # desde " primerlinea[0] ", hasta " primerlinea[1] ", con el PRECIO "int(primerlinea[3]"
    #minimo costo de s a t: minimo_precio esta mas arriba en este .py
    menor_precio = minimo_precio(grafo_precio, desde, hasta) 
    
    return cuello, menor_precio
    
    
if __name__ == '__main__':
    
    grafo_pesos=Grafo()
    
    #voy leyendo y agregando cada nodo en el grafo, agrego desde donde a donde y el peso
    with open("../rutas.txt") as archivo:
        for linea in archivo:
            primerlinea= linea.rstrip().split(',')
            grafo_pesos.agregar_arista(primerlinea[0], primerlinea[1], int(primerlinea[2]))
            # desde " primerlinea[0] ", hasta " primerlinea[1] ", con la ponderacion "int(primerlinea[2]"
   

    cuellodebotella, menor_costo = transportar_por (grafo_pesos, 'CiudadBs.As.', 'SanSalvadorJujuy')
    print ('El máximo peso a transportar es de:', cuellodebotella, 'Kg',  '\n' ,'El costo mínimo es: $', menor_costo,'000  ')
    
