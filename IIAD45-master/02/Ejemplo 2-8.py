# -*- coding: utf-8 -*-
"""
Ejemplo 2-8. Una clase base abstracta
"""

class Secuencia(metaclass=ABCMeta):
    
    @abstractmethod
    def __len__(self):
        
    @abstractmethod
    def __getitem__(self, j):
        
    def 
