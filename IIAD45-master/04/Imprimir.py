# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:25:32 2021

@author: IVAN
"""
def imprimir(n):
    
    if n == 0:
        return
    imprimir(n-1)
    print(n)
    