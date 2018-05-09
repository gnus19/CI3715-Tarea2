'''
Created on May 7, 2018

@author: andre
'''
from datetime import datetime, date, time, timedelta

class calcularPrecio:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''


    def calcularPrecio(self, tarifas, fechasDeServicio = []):
        tiempoDeServicio = fechasDeServicio[1] - fechasDeServicio[0]
        if (tiempoDeServicio.seconds/60 >= 15):
            return tarifas.tarifaNormal*((tiempoDeServicio.seconds//3600) + 1)
        else:
            pass
    
tiempoI = datetime.strptime('Jun 01 2005 23:50', '%b %d %Y %H:%M')
tiempoF = datetime.strptime('Jun 02 2005 00:10', '%b %d %Y %H:%M')
print((tiempoF - tiempoI).seconds/60)