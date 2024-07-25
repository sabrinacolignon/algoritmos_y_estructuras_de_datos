# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 09:59:56 2022

@author: Sabrina
"""

from modulos.LDE import Nodo, ListaDobleEnlazada
import random
import itertools
import time
import matplotlib.pyplot as plt

lista=ListaDobleEnlazada()
tiempos=[]
numero_iteraciones=1000


ns=[r+1 for r in range(numero_iteraciones)]

for i in range(len(ns)):
     tic = time.perf_counter()
     lista.insertar(i, random.randint(0,100))
     combinaciones = list(itertools.combinations(lista, i))
     lista.ordenar()
     toc = time.perf_counter()
     delta = toc - tic
     tiempos.append(delta)

plt.plot ( ns, tiempos )
plt.title('Tiempo vs cantidad de elementos')
plt.ylabel('T(n) [s]')
plt.xlabel('n')

