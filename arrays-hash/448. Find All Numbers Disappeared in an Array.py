"""
# Solucao brute force: O(n^2) time e O(1) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(1,len(nums)+1):
            flag = 0
            for j in range(len(nums)):
                if i==nums[j]:
                    flag = 1
                    break
            if flag == 0:
                res.append(i)
        
        return res
"""

# Solução O(n) time e O(n) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hs = set()

        for i in range(len(nums)):
            hs.add(nums[i])
        
        res = []
        for i in range(1,len(nums)+1):
            if i not in hs:
                res.append(i)

        return res