# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 17:01:43 2021

@author: IVAN
"""
import sys

def patron(lista):
    contador=0
    aux=[]
    patron=[]
    tamaños=[]
    for i in range (1,len(lista)):
        pat=sys.getsizeof(aux)
        aux.append(pat)
        if aux[i-2]!=aux[i-1]:
            tamaños.append(pat)
            patron.append(contador)
            contador=1
        else:
            contador+=1
    return patron

m=[0]*10000000
print(f"\nEl tamaño cambia cada {patron(m)} veces\n")