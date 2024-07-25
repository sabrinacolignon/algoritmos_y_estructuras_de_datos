# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:00:30 2022

@author: Sabrina
"""

class MonticuloBinario:
    
    """Método para inicializar un montículo binario"""
    def __init__(self):
        self._lista=[0] #inicializo la lista en cero para facilitar la division
        self._tamanio=0 #inicializo el tamaño en cero realizar un seguimiento del tamaño actual del montículo
    
    """Método para retornar el tamaño del montículo binario"""
#métodos mágicos a aquellos métodos de un objeto que son llamados sin que nosotros
#lo hagamos explícitamente
    def __len__(self):
        return self._tamanio #retorna el tamaño del monticulo para ir actualizandolo
    
    """Método para iterar sobre el montículo"""
    def __iter__(self):
        return iter(self._lista) #itera el montículo, devuelve un iterable
    
    """Método para infiltrar un nuevo ítem hacia arriba en el árbol hasta donde sea necesario"""
    def infiltrar_arriba(self, i): #i: indice del item recien agregado
        while i//2 > 0: #comparo el indice//2 con cero->busco que no tenga un padre
            if self._lista[i] < self._lista[i//2]: #compara el ítem recién agregado con su padre
                temp = self._lista[i//2] 
                self._lista[i//2] = self._lista[i] 
                self._lista[i] = temp 
            i = i//2 #se actualiza el elemento a insertar
 
    """Método para agregar un ítem a una lista al final de la lista"""
    def insertar(self, k): 
        self._lista.append(k) #inserto elemento k al final de la lista
        self._tamanio +=1 #actualizo el tamaño
        self.infiltrar_arriba(self._tamanio) # infiltro hacia arriba para mantener la propiedad del monticulo

    """Método pque devuelve el ítem con el menor valor clave, eliminándolo del montículo. y restaurar el cumplimiento total de la estructura de montículo"""
    def eliminar_min (self):
        valor_eliminado=self._lista[1] #el segundo elemento(raiz) es el valor que se va a eliminar
        self._lista[1] = self._lista[self._tamanio] #se le asigna al segundo elemento el ultimo de la lista
        self._tamanio-=1 #se actualiza el tamaño de ls lista
        self._lista.pop() #pop() elimina y retorna el último elemento de la lista
        self.infiltrar_abajo(1) #llamo a infiltrar abajo y le mando el indice 1 de la lista donde esta el menor 
        return valor_eliminado #retorna el valor eliminado

    """Método para encontrar hijo menor"""
    def hijo_min(self, i):
        if i*2+1 > self._tamanio: # si el hijo derecho es mayor al tamaño de la lista
            return i*2 #retorno el hijo izquierdo
        else:
            if self._lista[i*2] < self._lista[i*2+1]: #comparo los dos descendientes
                return i*2 #si el izquierdo tiene menor valor devuelvo SU POSICION
            else:
                return i*2+1 #si el derecho tiene menor valor devuelvo SU POSICION

    """Método para infiltrar un nodo hacia abajo"""
    def infiltrar_abajo(self, i): #i es el elemento a eliminar-> primer indice de la lista:raiz->minimo
        """ intercambiar la raíz con su hijo que sea menor que la raíz.
        Después del intercambio inicial, podemos repetir el proceso de intercambio
        con un nodo y sus hijos hasta que el nodo sea intercambiado a una posición en el árbol
        donde ya sea menor que ambos. 
        muevo el nuevo nodo raíz a su posición correcta en el montículo """
    
        while i*2 <= self._tamanio: #comparo el 2*indice con el tamaño
            minimo_h = self.hijo_min(i) #busco el hijo minimo del elemento
            if self._lista [i] > self._lista[minimo_h]: #si el elemento a eliminar es mayor al minimo
                temp=self._lista[i] 
                self._lista[i] = self._lista[minimo_h] 
                self._lista[minimo_h] = temp 
            i=minimo_h #se actualiza el elemento a eliminar para que siga buscando el minimo
        

