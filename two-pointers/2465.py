class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        l = 0
        r = len(nums)-1

        seen = set()

        nums.sort()

        while l<r:
            media = (nums[l]+nums[r])/2 # Não precisa ser a média
            seen.add(media)

            l+=1
            r-=1
        
        return len(seen)
