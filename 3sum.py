"""
# Solução para o problema "3Sum" usando a abordagem de força bruta com três loops aninhados para encontrar todas as combinações únicas de três números que somam a zero.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        res.add(tuple([nums[i],nums[j],nums[k]]))
        
        return [list(r) for r in res]
"""

# Solução para o problema "3Sum" usando a abordagem de ordenação e ponteiros duplos para encontrar todas as combinações únicas de três números que somam a zero em tempo O(n^2).
# Time O(n^2) | Space O(n^2), dependendo do sorting algorithm tb
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res = []

        for i,v in enumerate(nums):
            if i>0 and v == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == -v:
                    res.append([v, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif nums[l] + nums[r] > -v:
                    r-=1
                else:
                    l+=1
            
        return res