# Implementacion revursiva del factorial

def factorial(number):
    if number == 0:
        
        return 1
    
    return number * factorial(number-1)

num = int(input('Digite un numero: '))

print(f'El factorial de {num} es: {factorial(num)}')