# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:43:16 2022

@author: Sabrina
"""

# manejo de excepciones:
#     try:
#         codigo que puede fallar
#     except:
#         lo que quiero q haga si ocurre el error
#     else:
#         cuando no se ejecuta el except
#     finally:
#         siempre se ejecuta
        
# ejemplo:
    
# try:
#     archivo=open('../datos/archivo.txt')
#     # lista=[1,2,3]
#     # print(lista[0])
# except FileNotFoundError: #solo-> corre el riesgo de que ignore otros errores
#     #print("el archivo no existe")
#     archivo=open('./datos/archivo.txt', 'w') 
#     archivo.write("escribo")
# # except IndexError as mensaje:
# #     print("indice fuera de rango")
# #     print(mensaje)
# else:
#     contenido=archivo.read()
#     print(contenido)
# finally:
#     archivo.close()
     

from excepciones_imc import NotZeroError

def calcular_imc(peso, altura):
    
    if altura<=0:
        raise NotZeroError ("altura debe ser mayor que cero")
    if peso<=0:
        raise NotZeroError("peso debe ser mayor a cero")
    
    imc=peso/(altura**2)
    return round(imc, 2)
    
if __name__== '__main__':
    try:
        peso=int(input("ingrese peso: "))
        altura=float(input("ingrese altura: "))
        imc=calcular_imc(peso, altura)
    except NotZeroError as msg:
        print(msg)
    except ValueError:
        print("ingrese valores numericos")
    
    print("su imc es:", imc)