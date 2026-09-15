# Solução O(n log n) time and O(1) space
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l = 0
        r = k-1

        nums.sort()
        menor = float('inf')

        while r < len(nums):
            diff = nums[r] - nums[l]
            menor = min(menor, diff)

            r += 1
            l += 1

        return menor