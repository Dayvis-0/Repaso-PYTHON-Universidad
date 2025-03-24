# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:45:23 2021

@author: IVAN
"""

class Fraccion:
    """Clase que representa una fracción como numerador/denominador
    así como las operaciones básicas para fracciones
    
    
    """
    
    def __init__(self, num, den=1):
        """Instancia una fracción en base a un numerador y denominador,
        si no se pone denominador se asume como 1
        
        num:    numerador de tipo int
        den:    denominador de tipo int
        """
        if not isinstance(num,int) or not isinstance(den, int):
            raise TypeError("Numerador y denominador deben ser int")
        if den == 0:
            raise ValueError("Denominador no puede ser 0")
        self.__numerador = num
        self.__denominador = den
    
    def simplificar(self):
        """Simplifica  una fracción utilizando el mcd"""
        num = self.__numerador
        den = self.__denominador
        mcd = self.__mcd(num, den)
        self.__numerador = int(num/mcd)
        self.__denominador = int(den/mcd)
        return self
    
    def __mcd(self, a, b):
        while a:
            a, b = b % a, a
        return b
    
    def __str__(self):
        """Devuelve un str que muestra la fracción como numerador/denominador"""
        return str(self.__numerador) + "/" + str(self.__denominador)
    
    def __pow__(self, n):
        num = self.__numerador**abs(n)
        den = self.__denominador**abs(n)
        if n < 0:
            num, den = den, num
        return Fraccion(num, den)
    
    def __mul__(self, otra):
        """Sobrecarga el operador de multiplicacion * y devuelve un
        objeto Fraccion con el resultado de la operacion
        
        otra:   Una instancia de Fraccion que hará de multiplicando
        """
        if isinstance(otra, int):
            otra = Fraccion(otra)
        
        num = self.__numerador * otra.__numerador
        den = self.__denominador * otra.__denominador
        resultado =  Fraccion(num, den)
        resultado.simplificar()
        return resultado
       
    def __truediv__(self, otra):
        """Sobrecarga el operador division / y devuelve un objeto
        Fraccion con el resultado de la operación
        
        otra: Una instancia de Fraccion que hará de divisor
        """
        return self.__mul__(otra**-1)
    
    def __add__(self, otra):
        """ Sobrecarga el operador de adición + y devuelve un objeto
        Fraccion con el resultado de la operacion
        
        otra: Una instancia de Fracción que hara de segundo sumando
        """
        if isinstance(otra, int):
            otra = Fraccion(otra)
        den = self.__denominador * otra.__denominador
        num = otra.__denominador*self.__numerador + self.__denominador*otra.__numerador
        resultado = Fraccion(num,den)
        resultado.simplificar()
        return resultado
    
    def __sub__(self, otra):
        """Sobrecarga del operador de sustraccion -, devuelve un objeto
        Fraccion con el resultado del la operacion
        
        otra:   Una instancia de Fraccion que hara de sustraendo
        """
        return self.__add__(-otra)  #cambiando el signo y sumando
    
    def __neg__(self):
        """Sobrecarga el operador unario - que hace negativa una Fraccion"""
        num = -self.__numerador
        return Fraccion(num,self.__denominador)
    
    def __eq__(self, otra):
        yo = Fraccion(self.__numerador, self.__denominador)
        tu = Fraccion(otra.__numerador, otra.__denominador)
        yo.simplificar()
        tu.simplificar()
        if yo.__numerador == tu.__numerador and yo.__denominador == tu.__denominador:
            return True
        return False
    
    def set_num(self, num):
        self.__numerador = num
        
    def set_den(self, den):
        self.__denominador = den
        
    def get_num(self):
        return self.__numerador
    
    def get_den(self):
        return self.__denominador
        
