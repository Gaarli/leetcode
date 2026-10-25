class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        menor = float('inf')
        nums.sort()

        l = 0
        r = len(nums)-1

        while l<r:
            media = (nums[r]+nums[l])/2
            menor = min(menor,media)

            l+=1
            r-=1

        return menor