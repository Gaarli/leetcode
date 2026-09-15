# Busca binária para encontrar o mínimo em um array ordenado

"""arr = [1,2,3,4,5,6,7]
arr = arr[::-1]

def find_min(arr):
    l = 0
    r = len(arr) - 1

    res = arr[0]
    while l<=r:
        m = (l+r)//2

        res = min(res, arr[m])

        if arr[l] <= arr[m]:
            r = m - 1
        else:
            l = m + 1

    return res

print(find_min(arr))

"""
# Brute force:
# min(arr) time O(n) | Space O(1)

# Busca binária para encontrar o mínimo em um array ordenado e rotacionado time O(log n) | Space O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[l]

        while l<=r:
            if nums[l] <= nums[r]:
                return min(res,nums[l])

            m = (l + r) // 2
            res = min(res,nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res