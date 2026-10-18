class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        hm = {}

        for n in nums:
            hm[n] = hm.get(n,0)+1

        res = 0
        for n in nums:
            if hm[n] == 1:
                res+=n

        return res