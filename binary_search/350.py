# Solução O(n+m) time and O(n+m) space
"""class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht1 = {}
        ht2 = {}

        res = []

        for i in range(len(nums1)):
            ht1[nums1[i]] = 1 + ht1.get(nums1[i], 0)

        for j in range(len(nums2)):
            ht2[nums2[j]] = 1 + ht2.get(nums2[j], 0)

        for key, value in ht1.items():
            if key in ht2:
                for k in range(min(ht1[key], ht2[key])):
                    res.append(key)

        return res"""
# Solução O(n+m) time and O(n) space
# Tem como otimizar o space colocando o menor array no hash table
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht1 = {}

        res = []

        for i in range(len(nums1)):
            ht1[nums1[i]] = 1 + ht1.get(nums1[i], 0)

        for j in range(len(nums2)):
            if nums2[j] in ht1 and ht1[nums2[j]] > 0:
                res.append(nums2[j])
                ht1[nums2[j]] -= 1

        return res
        