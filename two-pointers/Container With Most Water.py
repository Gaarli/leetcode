"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute force O(n^2)

        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                water = (j-i) * min(height[i], height[j])
                res = max(res, water)

        return res

"""

# O(n) time usando two pointers

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        l = 0
        r = len(height)-1

        while l<r:
            water = (r-l) * min(height[l], height[r])
            res = max(res,water)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return res