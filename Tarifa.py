'''
Created on May 7, 2018

@author: Angel
'''
    
class Tarifa:
    '''
    classdocs
    '''
    tarifaNormal = 0
    tarifaFinDeSemana = 0

    def __init__(self, tarifaNormal, tarifaFinDeSemana):
        '''
        Constructor
        '''
        self.tarifaNormal = tarifaNormal
        self.tarifaFinDeSemana = tarifaFinDeSemana