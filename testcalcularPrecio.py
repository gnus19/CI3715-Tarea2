'''
Created on May 7, 2018

@author: andre
'''
import unittest

from calcularPrecio import calcularPrecio
from Tarifa import Tarifa
class calcularPrecioTest(unittest.TestCase):
    

    def setUp(self):
        self.tarifa = Tarifa(5, 10)
        self.clase = calcularPrecio(self.tarifa, [15, 20])
    
    def testcalculo(self):
        self.assertEquals(20, self.clase.calculo())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
