# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:36:19 2022

@author: Sabrina
"""

from modulos.circulo import Circulo
import unittest

class TestCirculo(unittest.TestCase):
    
    def setUp(self):
        self.c1=Circulo(4) #con esto evito crear un nuevo objeto ya que este pertenece a la clase
        #se llamaa dos veces porque se llama antes de cada prueba
        #los creo una vez y no tengo que estar creandolos dentro de cada metodo
    
    def test_area(self):
        #c1=Circulo(4)
        self.assertEqual(self.c1.area, 50.27) #(control, lo que debe dar como resultado)
        self.assertAlmostEqual(self.c1.area, 50.27, 2)# para los flotantes, el ultimo valor es la cantidad de decimales quiero comprobar
     
    def test_perimetro(self):
        #c1=Circulo(4)
        self.assertEqual(self.c1.perimetro, 25.13)
        
    def test_excepciones(self):
        print("test excepciones:")
        self.assertRaises(KeyError, self.c1.set_radio, -4) #excepcion esperada, atributo donde va a pasar, valor que va a causar la excepcion
    
    def tearDown(self): #mas que nada para cerrar bases de datos o archivos
        print("tear down: ")
        
         
if __name__ == '__main__':
    unittest.main()
        