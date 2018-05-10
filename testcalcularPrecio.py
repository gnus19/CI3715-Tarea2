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
    
    #Esta prueba es equivalente a verificar si en la clase existe la funcion
    def testTiempoDeServicioCero(self):
        self.assertEquals(None, self.clase.calcularPrecio(self.tarifa, [self.tiempoI, self.tiempoF]))
        
    def testMinTiempoDeServicio(self):
        self.tiempoI = datetime.strptime('Jun 01 2005 19:00', '%b %d %Y %H:%M')
        self.tiempoF = datetime.strptime('Jun 01 2005 19:15', '%b %d %Y %H:%M')
        self.assertEquals(5, self.clase.calcularPrecio(self.tarifa, [self.tiempoI, self.tiempoF]))
        
    def test14Min(self):
        self.tiempoI = datetime.strptime('Jun 01 2005 19:00', '%b %d %Y %H:%M')
        self.tiempoF = datetime.strptime('Jun 01 2005 19:14', '%b %d %Y %H:%M')
        self.assertEquals(None, self.clase.calcularPrecio(self.tarifa, [self.tiempoI, self.tiempoF]))

        
    def test16Min(self):
        self.tiempoI = datetime.strptime('Jun 01 2005 19:00', '%b %d %Y %H:%M')
        self.tiempoF = datetime.strptime('Jun 01 2005 19:16', '%b %d %Y %H:%M')
        self.assertEquals(5, self.clase.calcularPrecio(self.tarifa, [self.tiempoI, self.tiempoF]))
    
    def testTarifaNegativa(self):
        self.tarifa = Tarifa(-5, 10)
        self.tiempoI = datetime.strptime('Jun 01 2005 19:00', '%b %d %Y %H:%M')
        self.tiempoF = datetime.strptime('Jun 01 2005 19:16', '%b %d %Y %H:%M')
        self.assertEquals(None, self.clase.calcularPrecio(self.tarifa, [self.tiempoI, self.tiempoF]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
