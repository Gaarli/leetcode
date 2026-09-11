"""
# Brute force, time O(n*min(k,n)) e space O(1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, min(len(nums), i+k+1)):
                if nums[i] == nums[j]:
                    return True

        return False"""

"""# Solução O(n) e space O(n) usando hash table
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht = {}

        for i in range(len(nums)):
            if nums[i] in ht and i - ht[nums[i]] <= k:
                return True
            ht[nums[i]] = i

        return False

"""
# Solução com sliding window, O(n) e space O(min(n,k))
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = set()
        l = 0

        for r in range(len(nums)):
            if r-l > k:
                hs.remove(nums[l])
                l += 1
            if nums[r] in hs:
                return True
            else:
                hs.add(nums[r])
        
        return False