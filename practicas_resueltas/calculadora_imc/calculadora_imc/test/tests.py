# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:57:44 2022

@author: Sabrina
"""

from calculadora import Calculadora

class Testeo:
    
    def setUp(self):
        self.persona=Calculadora(55, 1.60)
    
    def test_altura(self):
        self.assertAlmostEqual(self.altura,)
