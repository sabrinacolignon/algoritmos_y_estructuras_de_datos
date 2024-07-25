
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:51:22 2022

@author: Sabrina
"""

from __future__ import annotations

class Nodo:
    def __init__(self, p_dato):
        """ Metodo inicializador de la clase Nodo,
        Inicializo siguiente y anterior en None y el dato es un parametro que envio, de tipo entero"""
        self._dato=p_dato
        self._siguiente=None
        self._anterior=None
        
    @property
    def dato(self):
        """ Metodo para devolver el valor del dato"""
        return self._dato
    @dato.setter
    def dato(self, p_dato):
        """ Metodo para configurar el valor del dato.
        recibe p_dato, entero."""
        self._dato=p_dato
    
    @property
    def siguiente(self):
        """ Metodo para devolver el valor del siguiente"""
        return self._siguiente
    @siguiente.setter
    def siguiente(self, p_siguiente):
        """ Metodo para configurar el valor del siguiente.
        recibe p_siguiente, entero."""
        self._siguiente=p_siguiente
    
    @property
    def anterior(self):
        """ Metodo para devolver el valor del anterior"""
        return self._anterior
    @anterior.setter
    def anterior(self, p_anterior):
        """ Metodo para configurar el valor del anterior.
        recibe p_anterior, entero."""
        self._anterior=p_anterior


class ListaDobleEnlazada:
    
    def __init__(self):
        """ Metodo inicializador de la clase ListaDobleEnlazada,
        Inicializo cabeza y cola en None y luego su tamanio en cero"""
        self._cabeza = None
        self._cola = None
        self._tamanio = 0
    
    @property
    def cabeza(self):
        """ Metodo para retornar el valor del dato en la cabeza"""
        return self._cabeza
    @cabeza.setter
    def cabeza(self, p_cabeza):
        """ Metodo para configurar el valor del dato en la cabeza.
        recibe p_cabeza, entero."""
        self._cabeza = p_cabeza
     
    @property
    def cola(self):
        """ Metodo para retornar el valor del dato en la cola"""
        return self._cola
    @cola.setter
    def cola(self, p_cola):
        """ Metodo para configurar el valor del dato en la cola
        recibe p_cola, entero."""
        self._cola = p_cola
        
    @property
    def tamanio(self):
        """ Metodo para retornar el tamaño de la lista"""
        return self._tamanio

    def esta_vacia(self):
        """ Metodo para saber si la lista esta vacia, returna True en dicho caso
            y False en caso de que no esté vacia
            Retorna: True o False"""
        return self._tamanio == 0      

    def __iter__(self):
        """ Metodo para iterar sobre la lista
        Retorna: None"""
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente  
    
    def __str__ (self):
        """ Metodo para retornar los valores de los datos en los nodos de la lista"""
        return str([nodo.dato for nodo in self])

    def agregar(self, p_item):
        """ Metodo para agregar un valor (item) al inicio de la lista,
        al finalizar actualiza el tamaño de la misma.
        recibe p_item, entero.
        Retorna: None"""
        temp = Nodo(p_item)
        
        if self.esta_vacia():
            self.cabeza = temp
            self.cola = temp
        else:
            temp.siguiente = self.cabeza
            self.cabeza.anterior = temp
            self.cabeza = temp
            
        self._tamanio +=1
     
    def anexar(self, p_item):    
        """ Metodo para anexar un valor (p_item) al final de la lista,
        al finalizar actualiza el tamaño de la misma.
        recibe p_item, entero.
        Retorna: None"""
        temp = Nodo(p_item)
        
        if self.esta_vacia():
            self.cabeza = temp
            self.cola = temp
            
        else:
            temp.anterior = self.cola
            self.cola.siguiente = temp
            self.cola = temp
        
        self._tamanio += 1
    
    def insertar(self, p_posicion, p_item):    
        """ Metodo para insertar un valor (p_item) en una posicion (p_posicion) de la lista,
        al finalizar actualiza el tamaño de la misma.
        Si la posicion esta por fuera de la lista emerge un mensaje de error.
        Recibe p_posicion y p_item, ambos enteros
        Retorna: None"""
        
        if p_posicion>self._tamanio or p_posicion<0:
            raise ValueError("La posicion a insertar esta fuera de rango")
           
        if p_posicion == 0:
            self.agregar(p_item)   
       
        elif p_posicion == self._tamanio: 
            nuevo = Nodo(p_item)    
            temp = self.cabeza
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.anterior = temp
            self._tamanio += 1
        
        else:
            nuevo = Nodo(p_item)
            temp = self.cabeza
            for i in range (p_posicion-1):
                temp = temp.siguiente
            aux = temp.siguiente
            nuevo.anterior = temp
            nuevo.siguiente = aux
            temp.siguiente = nuevo
            aux.anterior = nuevo
           
            self._tamanio += 1


    def extraer (self, p_posicion=-1):
        """ Metodo para extraer un valor en una posicion (p_posicion) de la lista y devuelve el item en posicion,
        si el parametro no esta indicado, se elimina y devuelve el ultimo elemnto de la lista
        al finalizar actualiza el tamaño de la misma.
        Si la posicion esta por fuera de la lista emerge un mensaje de error.
        recibe como parametro a p_posicion, un entero, si no lo recibe este es -1"""
        
        if self.esta_vacia():
            raise ValueError("La lista esta vacia")
        
        if p_posicion>=self._tamanio or p_posicion<-1:
            raise ValueError("La posicion a extraer esta fuera de rango")
        
        elif p_posicion == 0:
            aux = self.cabeza
            self.cabeza = self.cabeza.siguiente
            self._tamanio -=1
            return aux
        
        elif p_posicion == self._tamanio-1 or p_posicion == -1:
            aux = self.cola
            self.cola = self.cola.anterior
            self._tamanio -=1
            return aux
        
        else:
            temp = self.cabeza
            for i in range (p_posicion):
                temp = temp.siguiente
            aux = temp.anterior
            aux.siguiente = temp.siguiente
            temp.siguiente.anterior = aux
            self._tamanio -=1
            return temp

    def copiar(self):
        """ Metodo para copiar los elementos de la lista al final de una nueva lista,
        devuelve la copia de dicha lista"""
        copia = ListaDobleEnlazada()
        for nodo in self:
            copia.anexar(nodo.dato)
        return copia
        
    def invertir(self):
        """ Metodo para invertir el orden de los elementos de la lista.
        Si la lista esta vacia emerge un mensaje de error
        Retorna: None"""
        if self.esta_vacia():
            raise ValueError("La lista a invertir esta vacia")
        
        primer_nodo = self.cabeza
        cabeza_antes = self.cabeza
        segundo_nodo = primer_nodo.siguiente
        primer_nodo.siguiente = None
        primer_nodo.anterior = segundo_nodo
            
        while segundo_nodo != None:
            segundo_nodo.anterior = segundo_nodo.siguiente
            segundo_nodo.siguiente = primer_nodo
            primer_nodo = segundo_nodo
            segundo_nodo = segundo_nodo.anterior
        self.cabeza = primer_nodo
        self.cola=cabeza_antes

    
    def concatenar(self, l1 : ListaDobleEnlazada):
        """ Metodo para cocatenar dos listas doblemente enlazadas,
        Recibe una lista como argumento y retorna la lista actual habiendo cocatenado la que paso como parametro al final.
        al finalizar actualiza el tamaño de la misma.
        Si la posicion esta por fuera de la lista emerge un mensaje de error
        recibe como parametro a l1 es un objeto de tipo lista doblemente enlazada"""
        if l1.esta_vacia():
            raise IndexError("La lista a concatenar esta vacia")
            return self
        else:
            cabeza=l1.cabeza
            self.cola.siguiente = cabeza 
            l1.cabeza.anterior = self.cola
            self.cola = l1.cola
            self._tamanio += l1.tamanio
            return self
    
    def __add__(self, l1: ListaDobleEnlazada()):
        """Sobrecarga del operador suma para cocatenar dos listas doblemente enlazadas.
        recibe como parametro a l1 es un objeto tipo lista doblemente enlazada"""
        return self.cocatenar(l1)        
    
    def ordenar (self):
        """ Metodo para ordenar de menor a mayor los elementos de la lista.
        Si la lista esta vacia emerge un mensaje de error
        Retorna: None"""
        fin = None
        while self.cabeza != fin:
            actual = self.cabeza 
            temp = self.cabeza 
            while temp.siguiente != fin: 
                cambia = temp.siguiente 
                if temp.dato > cambia.dato:
                    temp.siguiente = cambia.siguiente 
                    cambia.siguiente = temp 
                    if temp != self.cabeza:
                        actual.siguiente = cambia 
                    else:
                        self.cabeza = cambia
                    aux = temp
                    temp = cambia 
                    cambia = aux 
                actual = temp 
                temp = temp.siguiente 
            fin=temp
        