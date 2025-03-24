"""Single Responsibility Principe (SRP)

Principio de responsabilidad unica:
Una clase debe tener una sola razon para cambiar, es decir, debe tener una unica responsabilidad.
En otras palabras, una clase debe estar enfocada en hacer una sola cosa y hacerla bien. Si una clase tiene multiples
responsabilidades, se vuelve mas dificil de mantener, porbar y entender"""

class UserDaataBase:
    def save(self, user):
        print(f'Guardando usuario {user} en la base de datos')
        
class EmailService:
    def send_welcome_email(self, user):
        print(f'Enviando correo de bienvenida a {user}')
        
user = 'Dayvis'

db = UserDaataBase()
email_service = EmailService()

db.save(user)
email_service.send_welcome_email(user)