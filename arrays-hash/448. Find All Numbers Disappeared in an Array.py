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