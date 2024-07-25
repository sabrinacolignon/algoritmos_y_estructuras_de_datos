# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:56:58 2022

@author: Sabrina
"""
from Nodo import Nodo
from __future__ import annotations

"""
LISTO: Crear una lista vacía (implementar inicializador).

Destruir la lista (implementar destructor).

Copiar la lista (implementar método “copiar”) para generar una copia profunda.

LISTO: Agregar un elemento en cualquier posición de la lista. La posición debe ser válida.

LISTO: Invertir el orden de los elementos de la lista.

Iterar sobre la lista.

LISTO: Ordenar de “menor a mayor” los elementos de la lista.
"""

class Lista:
    def __init__(self):
        self.cabeza=None
        self.tamanio=0
    
    @property
    def cabeza(self):
        return self._cabeza
    @cabeza.setter
    def cabeza(self, p_cabeza):
        self._cabeza=p_cabeza
    
    @property
    def tamanio(self):
        return self.tamanio
    
    def estaVacia(self):
        return self.cabeza is None
    
    def destructor(self):
        while self.cabeza!= None: #recorro la lista
            self.agregar("None")
    
    
    #https://www.techiedelight.com/es/clone-given-linked-list/
    def copiar(self, nuevaLista:Lista): #La función # toma una lista enlazada y devuelve su copia completa
        actual=self.cabeza # utilizado para iterar sobre la lista original
        nuevaLista=None # cabeza de lista nueva
        nuevaLista.cola=None # apunta al último nodo en una nueva lista
        while actual:
            if nuevaLista is None:
                nuevaLista=Nodo(actual.dato)#primer nodo nuevo
                nuevaLista.cola=nuevaLista
            else:
                nuevaLista.cola.siguiente=Nodo()
                nuevaLista.cola= nuevaLista.cola.siguiente
                nuevaLista.cola.dato=actual.dato
                nuevaLista.cola.siguinete=None
            actual=actual.siguiente
        return nuevaLista

    def agregar(self, item, pos):
        nuevo_nodo=Nodo(item)
        if self.estaVacia():
            self.cabeza=nuevo_nodo
        else:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza=nuevo_nodo
        self.tamanio+=1
        
    def invertir(self):
       prev = None
       actual = self.cabeza
       while actual is not None:
           next = actual.siguiente
           actual.siguiente = prev
           prev = actual
           actual = next
       self.cabeza = prev
    
    def iterador(self):
        nodo=self.cabeza
        while nodo:
            yield nodo
            nodo=nodo.siguiente
        
    def ordenar(self):
        fin = None
        while fin != self.cabeza:
            r=p=self.cabeza #variables que toman la posicion de inicio
            while p.siguiente != fin:
                q=p.siguiente #Q pasa a ser el siguiente de P
                if p.dato > q.dato:
                    p.siguiente=q.siguiente #el siguiente de p es el siguiente de q
                    q.siguiente=p #q siguiente toma la posicion de p
                    if p!=self.cabeza:
                        r.siguiente=q #el siguiente de r toma la posicion de q
                    else:
                        self.cabeza=q
                    aux=p
                    p=q #p toma la posicion de q
                    q=aux #q toma la posicion de aux
                r=p #r toma la posicion de p
                p=p.siguiente #p toma la posicion de su siguiente
            fin=p
                    
                