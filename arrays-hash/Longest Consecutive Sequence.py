# Solucao O(n) time e O(n) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)

        res = 0
        for num in hs:
            if num-1 in hs:
                continue
            else:
                length = 0
                curr = num
                while curr in hs:
                    curr += 1
                    length += 1
            res = max(res,length)

        return res
