# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:56:02 2022

@author: Sabrina
"""

# archivo=open("../datos/nombres.txt")
# contenido=archivo.read()
# print(contenido)
# archivo.close()

# with open ("../datos/nombres.txt") as archivo:
#     for linea in archivo:
#         print(linea, end="")

#abro el archivo de texto
with open ("../datos/nombres.txt") as archivo:
    contenido=archivo.readlines()
    print(contenido)
    
with open ("../datos/archivo_nuevo.txt", 'w') as archivo:
    escrito=archivo.write("es un archivo nuevo.")
    print(escrito)

#escribo nuevo archivo para que no se sobre escriba-> a
with open ("../datos/archivo_nuevo.txt", 'a') as archivo:
    escrito=archivo.write("es un archivo nuevo.")
    print(escrito)

#leo y escribo archivo:
with open ("../datos/archivo_nuevo.txt", 'r+') as archivo:
    archivo.read()
    escrito=archivo.write("escriboooo")
    print(escrito)
