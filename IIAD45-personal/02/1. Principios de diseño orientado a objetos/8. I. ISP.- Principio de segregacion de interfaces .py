"""Interface Segregation Principle (ISP)

Principio de Segregacion de interfaces
Los clientes no deben depender de interfaces que no usan. Es mejor tener muchas interfaces pequeñas y especificas que una grande.
En otras palabras, es mejor tener muchas interfaces pequeñas y especificas que una sola interfaz grande y general."""

from abc import ABC, abstractmethod

class PrintOnly(ABC):
    @abstractmethod
    def print(self):
        pass

class ScanOnly(ABC):
    @abstractmethod
    def scan(self):
        pass
    
class SimplePrinter(PrintOnly):
    def print(self):
        print('Printing')
    
class MultiFunctionPrinter(PrintOnly, ScanOnly):
    def print(self):
        print('Printing')
        
    def scan(self):
        print('Scanning')
        
printer = SimplePrinter()
printer.print()