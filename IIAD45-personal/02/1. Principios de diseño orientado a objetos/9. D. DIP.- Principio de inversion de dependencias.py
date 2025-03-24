"""Dependency Inversion Principle (DIP)

Principio de Invversion de Dependencias:
Los modulos de alto nivel no deben depender de modulos de bajo nivel. Ambos deben depender de abstracciones. Ademas, las abstracciones 
no deben depender de detalles. Los detalles deben depender de abtracciones
En otras palabras, el principio promueve que el diseño de un sistema debe basarse en abstracciones (interfaces o clases abtractas) en 
lugar de implementaciones concretas."""

from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, massage):
        pass
    
class EmailService(NotificationService):
    def send(self, massage):
        print(f'Enviando email: {massage}')
        
"""class SMSService(NotificationService):
    def send(self, massage):
        print(f'Enviandoo SMS: {massage}')"""
        
class NotificationManager:
    def __init__(self, service:NotificationService):
        self.service = service
        
    def notify(self, massage):
        self.service.send(massage)
        
email_service = EmailService()
#sms_service = SMSService()

notification_manager = NotificationManager(email_service)
notification_manager.notify('Hola por email')
