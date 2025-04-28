"""Dada una matriz de enteros nums y un numero entero target, regreso indices de los dos numeros de tal manera que sumen target
Puede suponer que cada entrada tendria exatamente una solucion y no puede  usar el igual dos veces
Puede devolver la respuesta en cualquier orden
Ejemplo 1:
#*  Entrada: nums = [2,7,11,15], target = 9
#*  Salida: [0,1]
#*  Explicacion: Porque nums[0] + nums[1] == 0, volvemos [0,1]."""
"""
#! Primera solucion
class Solution:
    def twoSum(self, nums, target):
        
        for n in range(len(nums)):
            aux = n+1
            if nums[n] + nums[aux] == target:
                return [n,aux]
    
nums = [2,7,11,15]
target = 9

sol = Solution()

soluci = sol.twoSum(nums, target)

print(soluci)
"""

#! Segunda solucion

class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in hashmap:
                return [j, hashmap[complement]]
            hashmap[nums[j]] = j
        
        return []

solu = Solution1()

nume = [1,2,4,5]
target = 7

print(solu.twoSum(nume, target))