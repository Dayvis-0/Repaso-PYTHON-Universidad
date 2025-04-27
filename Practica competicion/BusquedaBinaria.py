"""Complejidad
temporal - O(log n)
espacial - O(log n)"""
# Busqueda con recursividad
def busq_bina(S, target, low, high):
    if low > high:
        return False
    else:
        
        mid = (low + high) // 2

        if S[mid] == target:
            return True
        elif target < S[mid]:
            return busq_bina(S,target, low, mid-1)
        else: 
            return busq_bina(S, target, mid+1, high)
        
# Busqueda con iteracion
def busq_bina1(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid =  (low + high) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target :
            low = mid + 1
        else:
            high = mid - 1
            
    return False
        
# Busqueda con iteracion y indice
def busq_bina2(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

nume = [1,2,3]
busq = int(input("Numero a buscar: "))

# print(busq_bina(nume, busq, 0, len(nume)-1))
print(busq_bina2(nume, busq))
"""
if busq_bina(nume, busq, 0, len(nume)-1):
    print("Si")
else:
    print("no")"""