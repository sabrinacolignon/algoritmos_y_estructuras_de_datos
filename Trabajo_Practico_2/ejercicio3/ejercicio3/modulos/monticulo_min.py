# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:26:44 2022

@author: Mica
"""
# fijte si es de maximos o de minimos

class ColaDePrioridad:
    
    def __init__(self):
        ''''es una lista de tuplas ya que el algoritmo de dijkstra lo requiere'''
        self._lista=[(0,0)] #la cola es una LISTA DE TUPLAS
        self._tamanio=0
    
    @property
    def tamanio(self):
        return self._tamanio
    
    def __len__(self):
        return self._tamanio
    
    def __iter__(self):
        return iter(self._lista)
    
    def infiltrar_arriba(self, i):
        while i//2 > 0:
            #comparo la distancia
            if self._lista[i][0] < self._lista[i//2][0]:
                temp = self._lista[i//2]
                self._lista[i//2] = self._lista[i]
                self._lista[i] = temp
            i = i//2    
            
    def construir_monticulo(self,unaLista):
        i = len(unaLista) // 2 #se para en la mitad
        self._tamanio = len(unaLista) #el tamaño es la lista completa
        self._lista = [0] + unaLista[:] #el primer elemento del monticulo siempre es cero
        while (i > 0): #i = 1:​​estamos infiltrando hacia abajo desde la raíz del árbol->requerir múltiples intercambios
            self.infiltrar_abajo(i) #asegura que el hijo más grande siempre es desplazado hacia abajo
            i = i - 1 #decremento la mitad    
        
    def esta_vacia(self):
        return self._tamanio==0
    
    def insertar(self, k):
        self._lista.append(k)
        self._tamanio +=1
        self.infiltrar_arriba(self._tamanio)
    
    def hijo_min(self, i):
        if i*2+1 > self._tamanio:
            return i*2
        else:
            if self._lista[i*2][0] < self._lista[self._tamanio][0]:
                return i*2
            else:
                return i*2+1

    def infiltrar_abajo(self, i):
        while i*2 <= self._tamanio:
            minimo_h = self.hijo_min(i)
            if self._lista [i][0] > self._lista[minimo_h][0]:
                temp=self._lista[i]
                self._lista[i] = self._lista[minimo_h]
                self._lista[minimo_h] = temp
            i=minimo_h
        

    def eliminar_min (self):
        valor_eliminado=self._lista[1][1]
        self._lista[1] = self._lista[self._tamanio]
        self._tamanio-=1
        self._lista.pop()
        self.infiltrar_abajo(1)
        return valor_eliminado
    
    def devolver_minimo(self):
        return self.lista[1][1]
    
    
    def decrementar_clave (self, valor, nuevaclave): #valor=vertice
        #recorrer la lista e intercambiar la clave de un nodo por otra deseada,
        #infiltrando hacia arriba si es necesario para mantener la prioridad deseada
        hecho = False
        i = 1
        clave =0
        #busco el vertice
        while not hecho and i<=self._tamanio:
            if self._lista[i][1] == valor:
                hecho = True
                clave = i 
            else:
                i = i + 1
        if clave >0:
            self._lista[clave]= (nuevaclave, self._lista[clave][1])#agrega la clave y la infiltra
            self.infiltrar_arriba(clave)
    
    def __contains__ (self, vertice):
        #sirve para saber si un elemento existe en el objeto
        for par in self._lista:
            if par[1]==vertice:
                return True
        return False
    