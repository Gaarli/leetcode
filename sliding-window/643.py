"""
# Brute force O(n*k) space O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        for i in range(len(nums) - k + 1):
            soma = nums[i]
            for j in range(i+1, i + k):
                soma += nums[j]
            res = max(soma,res)
        
        return res/k
"""

# Usando sliding window, O(n) time e O(1) space

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = soma = sum(nums[:k])
        l = 0

        for r in range(k,len(nums)):
            soma -= nums[l]
            l+=1

            soma += nums[r]

            res = max(res, soma)
        
        return res/k