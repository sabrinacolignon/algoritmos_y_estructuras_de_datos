# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:57:36 2022

@author: Sabrina
"""

from aplicaciones.Temperaturas_DB import Temperaturas_DB
import unittest
from unittest.mock import patch
import io


class TestTemperatura(unittest.TestCase):
    
    
    """Definimos los registros utilizados para el test"""
    def setUp(self):
        self.registro_1 = Temperaturas_DB()
        self.registro_2 = Temperaturas_DB()
        self.registro_3 = Temperaturas_DB()
        
    
    """Test que comprueba el funcionamiento de los metodos guadar, borrar y mostrar cantidad de nodos"""
    def test_guardar_borrar(self):
        self.registro_1.guardar_temperatura("13/09/2022", 24)
        self.registro_1.guardar_temperatura("16/03/2022", 29)
        self.registro_1.guardar_temperatura("06/04/2022", 20)
        
        """Compruebo que el número de nodos creados sea correcto luego de guardarlos"""
        self.assertEqual(self.registro_1.mostrar_cantidad_muestras(), 3)
        self.registro_1.borrar_temperatura("13/09/2022")
        
        """Compruebo que el número de nodos en el arbol sea correcto luego de borrar uno"""
        self.assertEqual(self.registro_1.mostrar_cantidad_muestras(), 2)
        
        
    """Test que comprueba el método que devuelve la temperatura máxima entre dos fechas"""
    def test_temperatura_maxima(self):
        self.registro_2.guardar_temperatura("20/05/2012", 14.3)
        self.registro_2.guardar_temperatura("14/12/2013", 20.1)
        self.registro_2.guardar_temperatura("10/01/2015",35.7)
        self.registro_2.guardar_temperatura("02/09/2022", 24.4)
        
        """Compruebo que el valor máximo en el periodo denifinido sea el correcto"""
        self.assertEqual(self.registro_2.max_temp_rango("20/05/2012", "2/09/2022"), 35.7)
        
        """Compruebo caso donde la temperatura máxima se encuentre en el extremo inferior"""
        self.registro_2.guardar_temperatura("14/05/2012", 50) 
        self.assertEqual(self.registro_2.max_temp_rango("14/05/2012", "2/09/2022"), 50)
        
        """Compruebo caso donde la temperatura máxima se encuentre en el extremo superior"""
        self.registro_2.guardar_temperatura("03/09/2022", 42)
        self.assertEqual(self.registro_2.max_temp_rango("20/05/2012", "03/09/2022"), 42)
        
        
    
    """Test que comprueba el método que devuelve la temperatura mínima entre dos fechas"""
    def test_temperatura_minima(self):
        self.registro_3.guardar_temperatura("21/10/2011", 14.6)
        self.registro_3.guardar_temperatura("07/11/2014", 16)
        self.registro_3.guardar_temperatura("03/06/2021", 4.6)
        self.registro_3.guardar_temperatura("09/07/2022", 2.5)
        
        """Compruebo que el valor mínimo en el periodo denifinido sea el correcto"""
        self.assertEqual(self.registro_3.min_temp_rango("21/10/2011", "09/07/2022"), 2.5)
        
        """Compruebo el caso donde la temperatura mínima se encuentra en el extremo inferior"""
        self.registro_3.guardar_temperatura("18/10/2011", 0.5)
        self.assertEqual(self.registro_3.min_temp_rango("18/10/2011", "09/07/2022"), 0.5)
        
        """Compruebo el caso donde la temperatura mínima se encuentra en extremo superior"""
        self.registro_3.guardar_temperatura("11/07/2022", 0.3)
        self.assertEqual(self.registro_3.min_temp_rango("21/10/2011", "11/07/2022"), 0.3)
        
        
    """Test que comprueba el método que devuelve la temperatura máxima y mínima en un periodo determinado"""
    def test_extremos_rangos(self):
        self.registro_2.guardar_temperatura("20/05/2012", 14.3)
        self.registro_2.guardar_temperatura("14/12/2013", 20.1)
        self.registro_2.guardar_temperatura("10/01/2015",35.7)
        self.registro_2.guardar_temperatura("02/09/2022", 24.4)
        
        self.registro_3.guardar_temperatura("21/10/2011", 14.6)
        self.registro_3.guardar_temperatura("07/11/2014", 16)
        self.registro_3.guardar_temperatura("03/06/2021", 4.6)
        self.registro_3.guardar_temperatura("09/07/2022", 2.5)
        
        """Compruebo que los valores de la temperatura para ese rango de fechas sean correctos"""
        self.assertEqual(self.registro_2.temp_extremos_rango("20/05/2012","02/09/2022"), (14.3, 35.7))
        self.assertEqual(self.registro_3.temp_extremos_rango("21/10/2011", "09/07/2022"), (2.5, 16))
          
    """Test que comprueba el método que devuelve las temperaturas guardadas en un rango de fechas"""
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostrar_temperaturas(self, mock_stdout):
        self.registro_1.guardar_temperatura("13/09/2022", 24)
        self.registro_1.guardar_temperatura("16/03/2022", 29)
        self.registro_1.guardar_temperatura("06/04/2022", 20)
        
        self.registro_1.mostrar_temperaturas("16/03/2022", "13/09/2022")
        self.assertEqual(mock_stdout.getvalue(), "['16/03/2022: 29°C', '06/04/2022: 20°C', '13/09/2022: 24°C']\n")

        
if __name__ == "__main__":
    unittest.main() 