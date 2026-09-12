"""
# Solucao brute force, O(n*m) time e O(min(n,m)) space
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1[i] not in res:
                        res.add(nums1[i])
                    break
        
        return list(res)

"""

# Solucao O(n+m) time e O(n+m) space
"""class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht1 = set(nums1)
        ht2 = set(nums2)

        res = []
        for n in ht2:
            if n in ht1:
                res.append(n)

        return res"""
