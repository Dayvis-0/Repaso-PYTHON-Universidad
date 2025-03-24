# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:36:34 2021

@author: IVAN
"""

from Fraccion import Fraccion

class FraccionMixta(Fraccion):
    
    def __init__(self, entero, numerador, denominador):
        super().__init__(numerador, denominador)
        self.__entero = entero

        
    def __str__(self):
        return str(self.__entero) + " " + super().__str__()
    
    def __mul__(self, otra):
        m1 = Fraccion(self.__entero*self.get_den()+self.get_num(), self.get_den())
        m2 = Fraccion(otra.__entero*otra.get_den()+otra.get_num(), otra.get_den())
        producto = m1 * m2
     
        return self.mix(producto)
    
    def mix(self, fracc):
        return FraccionMixta(fracc.get_num() // fracc.get_den(),
                                  fracc.get_num() % fracc.get_den(),
                                  fracc.get_den())

