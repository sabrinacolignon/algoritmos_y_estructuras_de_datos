# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:06:39 2022

@author: Sabrina
"""

class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        """ Método para inicializar un nodo de un árbol. Recibe:
            clave: valor del dato
            valor: valor relacionado a la clave
            En el caso de que quiera agregar un nodo que ya tiene padre e hijos:
                -izquierdo: valor del nodo izquierdo. The default is None.
                -derecho: valor del nodo derecho. The default is None.
                -padre: valor del nodo padre. The default is None."""
            
        self.clave = clave
        self.carga_util = valor
        self.hijo_izq = izquierdo
        self.hijo_der = derecho
        self.padre = padre
        self.factor_eq = 0

    """Método para obtener el factor de equilibrio de un nodo"""
    @property
    def factor_eq(self):
        return self._factor_eq
    
    """Método para modificar el factor de equilibrio de un nodo"""
    @factor_eq.setter
    def factor_eq(self, p_factor_eq):
        self._factor_eq= p_factor_eq

    """Método que retorna True al hijo izquierdo del nodo"""
    def tiene_hijoizq(self):
        return self.hijo_izq

    """Método que retorna True al hijo derecho del nodo"""
    def tiene_hijoder(self):
        return self.hijo_der

    """Método que retorna True si el nodo es hijo izquierdo"""
    def es_hijoizq(self):
        return self.padre and self.padre.hijo_izq == self

    """Método que retorna True si el nodo es hijo derecho"""
    def es_hijoder(self):
        return self.padre and self.padre.hijo_der == self

    """Método que retorna True si el nodo es raiz"""
    def es_raiz(self):
        return not self.padre
    
    """Método que retorna True si el nodo es hoja"""
    def es_hoja(self):
        return not (self.hijo_der or self.hijo_izq)

    """Método que retorna True si el nodo tiene algun hijo derecho o izquierdo"""
    def tiene_algunhijo(self):
        return self.hijo_der or self.hijo_izq

    """Método que retorna True si el nodo tiene ambos hijos"""
    def tiene_amboshijos(self):
        return self.hijo_der and self.hijo_izq

    """Método para reemplazar los datos de un nodo, recibe su clave, valor y mabos hijos"""
    def reemplazar_datodenodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.carga_util = valor
        self.hijo_izq = hizq
        self.hijo_der = hder
        
        if self.tiene_hijoizq():
            self.hijo_izq.padre = self
        if self.tiene_hijoder():
            self.hijo_der.padre = self

    """Método para encontrar el sucesor de un nodo"""
    def encontrar_sucesor(self):
        suc = None
        if self.tiene_hijoder(): #si tiene hijo derecho
            suc = self.hijo_der.encontrar_min() #retorno el minimo del arbol derecho
        else:
            if self.padre:#empiezo desde le padre
                if self.es_hijoizq(): #si es hijo izquierdo
                    suc = self.padre #su sucesor es su padre
                else:#si es hijo derecho
                    self.padre.hijo_der = None #el padre no tiene hijo derecho
                    suc = self.padre.encontrar_sucesor() #llamo recursivamente hasta que encuentro el sucesor del max elemento 
                    #o el nodo ya deje de ser el nodo del hijo derecho, ya encuentro el primer ancestro cuyo hizo uzq es ancestro del nodo que estamos considerando
                    self.padre.hijo_der = self
        return suc

    """Método para encontrar el nodo con menor valor de la rama izquierda"""
    def encontrar_min(self): #la clave de valor mínimo: es el hijo más a la izquierda del árbol
         actual = self
         while actual.tiene_hijoizq(): #sigue las referencias hijoizq en cada nodo del subárbol
             actual = actual.hijo_izq  #hasta que alcanza un nodo que no tiene un hijo izquierdo
         return actual

    """Método para mostrar clave y valor de un nodo"""
    def __str__(self):
        return str(self.clave) +": " + str(self.carga_util) + " ºC"
   
    """Método para iterar de forma inorden: subarbol izq, raíz, subarbol der"""
    def __iter__(self): #debe devolver sólo un nodo cada vez que se llama al iterador
        if self:
            if self.tiene_hijoizq():
                for elem in self.hijo_izq:
                    yield elem #congela el estado de la función para que la próxima vez que se llame a la función continúe ejecutándose desde el punto exacto donde quedó antes
            yield self
            if self.tiene_hijoder():
                for elem in self.hijo_der:
                    yield elem
    
    """Método para empalmar nodos"""
    def empalmar(self): #va directamente al nodo que queremos empalmar y hace los cambios correctos
       if self.es_hoja(): #si es nodo hoja:
           if self.es_hijoizq():
                  self.padre.hijo_izq = None
           else:
                  self.padre.hijo_der = None
       
       elif self.tiene_algunhijo(): 
           if self.tiene_hijoizq(): #si tiene hijo izquierdo
                  if self.es_hijoizq():
                     self.padre.hijo_izq = self.hijo_izq
                  else:
                     self.padre.hijo_der = self.hijo_izq
                  self.hijo_izq.padre = self.padre
           else:    #si tiene hijo derecho
                  if self.es_hijoizq():
                     self.padre.hijo_izq = self.hijo_der
                  else:
                     self.padre.hijo_der = self.hijo_der
                  self.hijo_der.padre = self.padre


class AVL:
    def __init__(self):
        """ Método inicializador para un arbol AVL """
        self.raiz = None
        self.tamanio = 0

    """Método que retorna el tamaño del arbol AVL"""
    def tamanio(self):
        return self.tamanio
    
    """Método que retorna la longitud del arbol AVL"""
    def longitud(self):
        return self.tamanio
    
    """Método que retorna para len()"""
    def __len__(self):
        return self.tamanio
    
    """Método para iterar el árbol AVL"""
    def __iter__(self):
        return self.raiz.__iter__()
    
    """Método para agregar nodos al árbol AVL, recibe su clave y valor"""
    def agregar(self, clave, valor):
       if self.raiz:
           self._agregar(clave, valor, self.raiz)
       else:
           self.raiz = NodoArbol(clave, valor) #si no tiene raíz la crea
       self.tamanio = self.tamanio + 1

    """Método privado para agregar un nodo al arbol según su clave, valor y ubicacion"""
    def _agregar (self, clave, valor, nodo_actual): #nodo_actual es la raíz
       if clave < nodo_actual.clave:
           if nodo_actual.tiene_hijoizq():
               self._agregar(clave, valor, nodo_actual.hijo_izq)
           else:
               nodo_actual.hijo_izq = NodoArbol(clave, valor, padre=nodo_actual)
               self.actualizar_equilibrio(nodo_actual.hijo_izq)
       
       else:
           if nodo_actual.tiene_hijoder():
               self._agregar(clave, valor, nodo_actual.hijo_der)
           else:
               nodo_actual.hijo_der = NodoArbol(clave, valor, padre=nodo_actual)
               self.actualizar_equilibrio(nodo_actual.hijo_der)
    
    """Método para actualizar el equilibio de un arbol luego de agregar o eliminar un nodo"""
    def actualizar_equilibrio (self, nodo):
    #si el nodo actual está lo suficientemente desequilibrado como para requerir el reequilibrio
       if nodo.factor_eq > 1 or nodo.factor_eq < -1: 
           self.reequilibrar(nodo) # se realiza el reequilibrio y no se requiere hacer ninguna nueva actualización a los padres
           return
       if nodo.padre != None: #Si el nodo actual no requiere reequilibrio
           if nodo.es_hijoizq():
                nodo.padre.factor_eq += 1
           elif nodo.es_hijoder():
                nodo.padre.factor_eq -= 1
           if nodo.padre.factor_eq != 0: #Si el factor de equilibrio del padre no es cero
               self.actualizar_equilibrio(nodo.padre)#continúa ascendiendo en el árbol, hacia la raíz
   
    """Método mágico para agregar clave y valor"""
    def __setitem__(self, c, v):
       self.agregar(c, v)

    """Método para obtener el valor a partir de una clave ingresada"""
    def obtener(self, clave):
       if self.raiz:
           res = self._obtener(clave, self.raiz)
           if res:
               return res.carga_util
           else:
               return None
    
    """Método privado para obtener el valor de un nodo a partir de una clave y nodo"""
    def _obtener(self, clave, nodo_actual):
       if not nodo_actual:
           return None
       
       elif nodo_actual.clave == clave:
           return nodo_actual
       
       elif clave < nodo_actual.clave:
           return self._obtener(clave, nodo_actual.hijo_izq)
       
       else:
           return self._obtener(clave, nodo_actual.hijo_der)
    
    """Método mágico para obtener el valor de una clave"""
    def __getitem__(self, clave):
       return self.obtener(clave) 

    """Método magico para saber si el nodo a obtener es la raiz"""
    # sirve para saber si un elemento existe en el objeto
    def __contains__(self, clave):
       if self._obtener(clave, self.raiz):
           return True
       else:
           return False           
         
    """Método para eliminar nodo a partir de su clave"""
    def eliminar(self, clave):
      if self.tamanio > 1: #arbol tiene mas de un nodo
        nodoAEliminar = self._obtener(clave, self.raiz) #encuentra el nodo
        if nodoAEliminar:
           self.remover(nodoAEliminar) #realiza las asignaciones correspondientes
           self.tamanio = self.tamanio-1
        else:
           raise KeyError('Error, la clave no está en el árbol')
       
      elif self.tamanio == 1 and self.raiz.clave == clave: #se elimina la raiz
           self.raiz = None
           self.tamanio = self.tamanio - 1
      
      else:
           raise KeyError('Error, la clave no está en el árbol')

    """Método mágico para eliminar nodo"""
    def __delitem__(self, clave): #si no se encuentra la clave, el operador del genera un error
        self.eliminar(clave)       
    
    """Método para remover un nodo según su posición en el arbol"""
    def remover(self, nodo_actual):
         if nodo_actual.es_hoja(): #nodo hoja
           if nodo_actual == nodo_actual.padre.hijo_izq:
               nodo_actual.padre.hijo_izq = None
           else:
               nodo_actual.padre.hijo_der = None
         
         #sustituye dicho nodo con el sucesor en inOrden-> nodo con el menor valor del subárbol derecho   
         elif nodo_actual.tiene_amboshijos(): #nodo interior con dos hijos
           suc = nodo_actual.encontrar_sucesor()
           suc.empalmar() #Para eliminar el sucesor
           nodo_actual.clave = suc.clave
           nodo_actual.carga_util = suc.carga_util

         else: ## este nodo tiene un (1) hijo
           if nodo_actual.tiene_hijoizq():
             if nodo_actual.es_hijoizq():
                 nodo_actual.hijo_izq.padre = nodo_actual.padre
                 nodo_actual.padre.hijo_izq = nodo_actual.hijo_izq
             elif nodo_actual.es_hijoder():
                 nodo_actual.hijo_izq.padre = nodo_actual.padre
                 nodo_actual.padre.hijo_der = nodo_actual.hijo_izq
             else: #Si el nodo actual no tiene padre, debe ser la raíz
                 nodo_actual.reemplazar_datodenodo(nodo_actual.hijo_izq.clave,
                                    nodo_actual.hijo_izq.carga_util,
                                    nodo_actual.hijo_izq.hijo_izq,
                                    nodo_actual.hijo_izq.hijo_der)
           else: 
             if nodo_actual.es_hijoizq():
                 nodo_actual.hijo_der.padre = nodo_actual.padre
                 nodo_actual.padre.hijo_izq = nodo_actual.hijo_der
             elif nodo_actual.es_hijoder():
                 nodo_actual.hijo_der.padre = nodo_actual.padre
                 nodo_actual.padre.hijo_der = nodo_actual.hijo_der
             else: #Si el nodo actual no tiene padre, debe ser la raíz
                 nodo_actual.reemplazar_datodenodo(nodo_actual.hijo_der.clave,
                                    nodo_actual.hijo_der.carga_util,
                                    nodo_actual.hijo_der.hijo_izq,
                                    nodo_actual.hijo_der.hijo_der)
    
    """Método para rotar a la izquierda a traves de un pivote que se pasa como parámetro"""
    def rotar_izq(self, rot_raiz):
        #variable temporal para realizar un seguimiento de la nueva raíz del subárbol
         nueva_raiz = rot_raiz.hijo_der #la nueva raíz es el hijo derecho de la raíz anterior
         rot_raiz.hijo_der = nueva_raiz.hijo_izq # reemplazo el hijo derecho de la raíz antigua con el hijo izquierdo de la nueva.
         
         #ajustar los punteros a los padres de los dos nodos
         if nueva_raiz.hijo_izq != None: #Si nuevaRaiz tiene un hijo izquierdo
             nueva_raiz.hijo_izq.padre = rot_raiz #el nuevo padre del hijo izquierdo se convierte en la raíz antigua
         nueva_raiz.padre = rot_raiz.padre #Al padre de la nueva raíz se le asigna el padre de la raíz antigua
         
         if rot_raiz.es_raiz(): #Si la raíz antigua era la raíz de todo el árbol
             self.raiz = nueva_raiz #asignar la raíz del árbol para que apunte a esta nueva raíz
         else:
             if rot_raiz.es_hijoizq(): #si la raíz antigua es un hijo izquierdo
                rot_raiz.padre.hijo_izq = nueva_raiz #cambiamos al padre del hijo izquierdo para que apunte a la nueva raíz
             else:
                 rot_raiz.padre.hijo_der = nueva_raiz #cambiamos al padre del hijo derecho para que apunte a la nueva raíz
         
            #actualizamos los factores de equilibrio de las raíces vieja y nueva
         nueva_raiz.hijo_izq= rot_raiz 
         rot_raiz.padre = nueva_raiz #asignamos la nueva raíz como padre de la raíz antigua
         
         rot_raiz.factor_eq = rot_raiz.factor_eq + 1 - min(nueva_raiz.factor_eq, 0)
         nueva_raiz.factor_eq = nueva_raiz.factor_eq + 1 + max(rot_raiz.factor_eq, 0)  
    
    """Método para rotar a la izquierda a traves de un pivote que se pasa como parámetro"""
    def rotar_der(self, rot_raiz):
         nueva_raiz = rot_raiz.hijo_izq 
         rot_raiz.hijo_izq = nueva_raiz.hijo_der
         
         if nueva_raiz.hijo_der != None:
             nueva_raiz.hijo_der.padre = rot_raiz
         nueva_raiz.padre = rot_raiz.padre
         
         if rot_raiz.es_raiz(): 
             self.raiz = nueva_raiz
         else:
             if rot_raiz.es_hijoizq():
                rot_raiz.padre.hijo_izq = nueva_raiz
             else:
                rot_raiz.padre.hijo_der = nueva_raiz

         nueva_raiz.hijo_der = rot_raiz
         rot_raiz.padre = nueva_raiz
         
         rot_raiz.factor_eq = rot_raiz.factor_eq - 1 - max(nueva_raiz.factor_eq, 0)
         nueva_raiz.factor_eq = nueva_raiz.factor_eq - 1 + min(rot_raiz.factor_eq, 0)
    
    """Método para reequilibrar los factores de equilibrio a partir de un nodo"""
    def reequilibrar(self, nodo):
    #Si un subárbol necesita una rotación a la izquierda para equilibrarlo:
          if nodo.factor_eq < 0: 
              if nodo.hijo_der.factor_eq > 0: #compruebo el fe del hijo derecho
                  self.rotar_der(nodo.hijo_der) #Si el hijo derecho es pesado a la izquierda entonces aplique una rotación a la derecha al hijo derecho
                  self.rotar_izq(nodo) #rotación a la izquierda original
              else:
                  self.rotar_izq(nodo) #sino rotacion simple a la izquierda
   
    #Si un subárbol necesita una rotación a la derecha para equilibrarlo:
          elif nodo.factor_eq > 0:
              if nodo.hijo_izq.factor_eq < 0: #compruebo el fe del hijo izquierdo
                  self.rotar_izq(nodo.hijo_izq) #Si el hijo izquierdo es pesado a la derecha, aplique una rotación a la izquierda al hijo izquierdo
                  self.rotar_der(nodo) #rotacion a la derecha original
              else:
                  self.rotar_der(nodo) #sino rotacion simple a la derecha
    
     
class Iterador:
    def __init__(self, p_arbol, p_clave_inicial):
        """ Clase iterador para poder iterar sobre un árbol AVL a través de sus nodos:
            Recibe: p_arbol : Arbol AVL sobre el cual voy a iterar
                    p_clave_inicial :  Clave del nodo a partir del cual voy a iterar """
        self.nodo = p_arbol._obtener(p_clave_inicial, p_arbol.raiz)
    
    """ Método iterador de la clase Iterador"""
    def __iter__(self): 
        return self

    """Método para recorrer y devolver un elemento del iterable indicado"""
    #recorre inorden porque utilizo el encontrar sucesor
    def __next__(self):
        salida=self.nodo
        
        if not self.nodo:   
            raise StopIteration

        self.nodo = self.nodo.encontrar_sucesor() 
        return salida
           
    