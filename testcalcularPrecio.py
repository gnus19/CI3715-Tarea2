'''
Created on May 7, 2018

@author: andre
'''
import unittest
from datetime import datetime, date, time, timedelta
from calcularPrecio import calcularPrecio
from Tarifa import Tarifa
class calcularPrecioTest(unittest.TestCase):
    

    def setUp(self):
        self.tarifa = Tarifa(5, 10)
        self.tiempoI = datetime.strptime('Jun 01 2005 19:05', '%b %d %Y %H:%M')
        self.tiempoF = datetime.strptime('Jun 01 2005 19:05', '%b %d %Y %H:%M')
        self.clase = calcularPrecio()
    
    def testCero(self):
        self.assertEquals(None, self.clase.calcularPrecio(self.tarifa, [self.tiempoI, self.tiempoF]))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
