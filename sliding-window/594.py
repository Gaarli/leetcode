class Solution:
    def findLHS(self, nums: list[int]) -> int:
        melhor = 0
        nums.sort()


        l = 0

        # Pelo menos 1 elemento
        for r in range(len(nums)):
            while nums[r] - nums[l] >1 and l+1<len(nums):
                l+=1
            
            if nums[r] - nums[l] ==1:
                melhor = max(melhor,r-l+1)

        return melhor

