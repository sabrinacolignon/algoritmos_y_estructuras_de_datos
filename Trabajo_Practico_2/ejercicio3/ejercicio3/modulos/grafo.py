# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:31:47 2022

@author: Mica
"""

class Vertice:
    # representará cada vértice en el grafo
    def __init__(self,clave):
        self.id = clave #normalmente será una cadena
        self.conectadoA = {} #inicializo diccionario
        self.dist = 0 #dist: maxima carga que puede llegar a ese nodo por algun camino
        self.predecesor = None

    def agregar_vecino(self,vecino,ponderacion=0): #ponderacion=0 si el grafo es no ponderado
        #agregar una conexión desde este vértice a otro
        self.conectadoA[vecino] = ponderacion #valor

    def __str__(self): 
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtener_conexiones(self):
        #devuelve todos los vértices de la lista de adyacencia,
        #representados por la variable conectadoA
        return self.conectadoA.keys()

    def obtener_id(self):
        return self.id

    def obtener_ponderacion(self,vecino):
        #devuelve la ponderación de la arista de este vértice al vértice pasado como parámetro.
        return self.conectadoA[vecino]
    
    def asignar_predecesor(self, vertice): #en el caso de recorrer y obtener ruta
        self.predecesor=vertice


class Grafo:
    #contiene la lista maestra de vértices
    def __init__(self):
        self.listaVertices = {} #diccionario que asigna nombres de vértices a objetos vértice
        self.numVertices = 0

    def agregar_vertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtener_vertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        #sirve para saber si un elemento existe en el objeto
        return n in self.listaVertices

    def agregar_arista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregar_vertice(de) #se le asigna a una variable para respetar el return del agregar_vertice
        if a not in self.listaVertices:
            nv = self.agregar_vertice(a)
        self.listaVertices[de].agregar_vecino(self.listaVertices[a], costo) #los agrega como vecinos

    def obtener_vertices(self):
        #devuelve los nombres de todos los vértices del grafo
        #permite iterar sobre los vertices de un grafo por nombre
        return self.listaVertices.keys()

    def __iter__(self):
        #facilita la iteración sobre todos los objetos vértice de un grafo en particular
        #permite iterar sobre los vertices de un grafo por sus mismos objetos
        return iter(self.listaVertices.values())
    
    