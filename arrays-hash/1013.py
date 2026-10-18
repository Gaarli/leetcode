# Solução O(n²) time e O(1) space
"""
 class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        for i in range(len(arr)-2):
            soma1 = sum(arr[:i+1])

            soma2 = 0
            p2 = i + 1
            while True:
                soma2 += arr[p2]
                if soma2==soma1 or p2 >= len(arr)-2:
                    break
                p2+=1
            
            soma3 = sum(arr[p2+1:])
            
            if soma1==soma2 and soma2==soma3:
                return True

        return False

 """

