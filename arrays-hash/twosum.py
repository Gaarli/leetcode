"""
# Solução para o problema "Two Sum" usando a abordagem de ordenação e ponteiros duplos.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []

        for i in range(len(nums)):
            arr.append([nums[i],i])
        
        arr.sort()

        l = 0
        r = len(nums)-1

        while l<r:
            sum = arr[l][0] + arr[r][0]
            if sum == target:
                i1 = arr[l][1]
                i2 = arr[r][1]
                menor = min(i1,i2)
                maior = max(i1,i2)
                return [menor,maior]
            elif sum > target:
                r -= 1
            else:
                l += 1
        
        return []
"""
# Solução para o problema "Two Sum" usando a abordagem de hash table (dicionário) para encontrar os índices dos números que somam ao alvo em tempo O(n).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i in range(len(nums)):
            complemento = target - nums[i]

            if complemento in ht:
                return [min(ht[complemento], i),
                max(ht[complemento], i)]
            elif nums[i] not in ht:
                ht[nums[i]] = i
            else:
                continue
        
        return []