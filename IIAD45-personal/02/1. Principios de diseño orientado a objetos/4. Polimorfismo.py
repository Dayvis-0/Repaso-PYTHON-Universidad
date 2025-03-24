"""El polimorfismo permite que objetos de diferentes clases sean tratados como oobjetos de una clase comun"""

class Bird:
    def fly(self):
        
        return 'Flying hight'
    
class Airplane:
    def fly(self):
        
        return 'Fly faster'
    
def let_it_fly(flying_object):
    print(flying_object.fly())
    
bird = Bird()
airplane = Airplane()

let_it_fly(bird)
let_it_fly(airplane)