
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:48:17 2022

@author: Mica
"""
from random import randint
import sys

def crear_archivo_de_datos(nombre):
    
    f = 10**6
    N = 5*f
    cifras = 20
    tam_bloque = f # 1 M de valores por bloque a escribir
    
    print('Cantidad de valores a escribir:', N)
    
    # truncar archivo si existe
    with open(nombre, 'w') as archivo:
        pass
    
    # escribir datos
    N_restantes = N
    while N_restantes > 0:
        cif = cifras
        r = N_restantes % tam_bloque
        c = N_restantes // tam_bloque
        if c > 0:
            t = tam_bloque
        elif c == 0:
            t = r
        N_restantes -= t
        print('t =', t, ', N_restantes =', N_restantes)
        bloque = [str(randint(10**(cif-1), 10**cif-1))+'\n'
                  for i in range(t)]        
        with open(nombre, 'a+') as archivo:
            archivo.writelines(bloque)
            


def dividir_archivos(unArchivo):
                  
    with open ('Aux1.txt', 'w') as auxiliaruno, open ('Aux2.txt', 'w') as auxiliardos, open (unArchivo) as archi:
        primero = archi.readline().rstrip('\n') 
        segundo= archi.readline().rstrip('\n')
                #abrí los 3archivos, los dos auxsi no existian los creo
        auxiliaruno.write(primero + '\n')
                #ya se que tengo que escribir el primer numero en el primer archivo 
        
        escribir_en_el_segundo = False
        '''mientras que no lea el fin del archivo '''
        while segundo!='':
            '''condicional para saber donde escribir'''
            if primero>segundo: 
                escribir_en_el_segundo = not escribir_en_el_segundo
            '''condicional para escribri donde corresponde''' 
            
            if escribir_en_el_segundo: 
                auxiliardos.write(segundo + '\n')
                  
            else:
                auxiliaruno.write(segundo + '\n')
                   
            primero = segundo
            segundo = archi.readline().rstrip('\n')
                                        
  

def mezclar_archivos(unArchivo, aux1, aux2):
    '''abro los dos archivos auxiliares para lectura y el archivo original para escritura ''' 
    with open (aux1, 'r') as auxiliaruno, open (aux2, 'r') as auxiliardos, open (unArchivo, 'w') as archi:
        '''Leo los dos primeros de cada auxiliar'''
        siguiente_aux1 = auxiliaruno.readline().rstrip('\n')
        siguiente_aux2 = auxiliardos.readline().rstrip('\n')
        '''este contador me va a servir para poder saber cuántas veces se repite el mezclar '''
        sublistas = 0
        '''mientras no sea el fin del archivo uno NI del archivo dos''' 
        ultimo='0'
        
        while siguiente_aux2 != '' and siguiente_aux1 != '':
           if siguiente_aux1 <= siguiente_aux2:
               if ultimo <= siguiente_aux1:
                   archi.write(siguiente_aux1 + '\n')
                   
                   ultimo = siguiente_aux1
                   siguiente_aux1 = auxiliaruno.readline().rstrip('\n') 
               elif ultimo <= siguiente_aux2:
                   archi.write(siguiente_aux2 + '\n') 
                   ultimo = siguiente_aux2
                   siguiente_aux2 = auxiliardos.readline().rstrip('\n')
               else:
                   sublistas += 1
                   archi.write(siguiente_aux1 + '\n')
                   ultimo = siguiente_aux1
                   siguiente_aux1 = auxiliaruno.readline().rstrip('\n')
                   
           else:
               if ultimo <= siguiente_aux2:
                   archi.write(siguiente_aux2 + '\n')
                   ultimo = siguiente_aux2
                   siguiente_aux2 = auxiliardos.readline().rstrip('\n')
               elif ultimo <= siguiente_aux1:
                   archi.write(siguiente_aux1 + '\n')
                   ultimo = siguiente_aux1
                   siguiente_aux1 = auxiliaruno.readline().rstrip('\n')
               else:
                   sublistas += 1
                   archi.write(siguiente_aux2 + '\n')
                  
                   ultimo = siguiente_aux2
                   
                   siguiente_aux2 = auxiliardos.readline().rstrip('\n')
        
        sublistas += 1            
    
        while siguiente_aux1 != '':
            if ultimo>siguiente_aux1:
                sublistas +=1
            archi.write(siguiente_aux1 +'\n')
            ultimo= siguiente_aux1
            siguiente_aux1 = auxiliaruno.readline().rstrip('\n')

        while siguiente_aux2 != '':
            if ultimo > siguiente_aux2:
                sublistas+=1
            archi.write(siguiente_aux2 +'\n')
            ultimo=siguiente_aux2
            siguiente_aux2 = auxiliardos.readline().rstrip('\n')


        return sublistas   
    
    
'''Esta funcion utiliza los metodos dividir y mezclar de manera recursiva'''        
def Ordenamiento_mezcla_natural(unArchivo):
    sublistas=0
    ''' si la sublista es =1 quiere decir que ya se termino de ordenar '''
    while sublistas !=1:
        dividir_archivos(unArchivo)
        sublistas= mezclar_archivos(unArchivo, 'Aux1.txt', 'Aux2.txt')
    
'''Esta funcion recibirá un archivo y devolver{a el tamaño en bytes del mismo'''
def Tamanio_de_archivo (unArchivo):
    tamanio = 0
    
    with open(unArchivo, 'r') as archi:
        for linea in archi:  
            tamanio += sys.getsizeof(linea)
    '''devuelvo el tamaño'''
    return tamanio 


'''Esta funci{on va a probar que el archivo resultante posea el mismo tamaño (en bytes) 
que el archivo original y que los datos en su interior están realmente ordenados 
de menor a mayor luego de aplicar el algoritmo'''  

def Prueba_ordenamiento (unArchivo, bytesoriginal):
    
    
    '''para comprobar el tamaño en bytes hice la funcion Tamanio_de_archivo'''
    nuevo_tamanio = Tamanio_de_archivo(unArchivo)
    if bytesoriginal==nuevo_tamanio:
        print('Los archivos tienen el mismo tamaño en bytes')
    with open(unArchivo, 'r') as archi:
        primer_dato = archi.readline().rstrip('\n')
        segundo_dato = archi.readline().rstrip('\n')
        while segundo_dato !='':
            if primer_dato > segundo_dato:
                print('LOS DATOS NO ESTÁN ORDENADOS')
                break
            primer_dato=segundo_dato
            segundo_dato=archi.readline().rstrip('\n')
    


    

if __name__ == '__main__':
    crear_archivo_de_datos('datos.txt')
    tam_original= Tamanio_de_archivo('datos.txt')
    Ordenamiento_mezcla_natural('datos.txt')
    Prueba_ordenamiento('datos.txt', tam_original)