# Solução brute force: O(n^2) time e O(1) space

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        flag = 0

        for i in range(len(nums)):
            flag = 0
            for j in range(len(nums)):
                if i!=j and nums[i] == nums[j]:
                    flag = 1
                    break
                
            if flag == 0:
                return nums[i]

"""
# Solução com hash table: O(n) time e O(n) space
ht = {}

        for i in range(len(nums)):
            ht[nums[i]] = 1 + ht.get(nums[i],0)

        for key, value in ht.items():
            if value==1:
                return key

"""
# Solucao usando hashset, O(n) time e O(n) space
hs = set()

for i in range(len(nums)):
    if nums[i] in hs:
        hs.remove(nums[i])
    else:
        hs.add(nums[i])

return list(hs)[0]

"""
    