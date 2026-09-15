"""
# Brute force, O(n) time and O(1) space
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            if ord(letters[i]) > ord(target):
                return letters[i]
        return letters[0]
"""
# Solucao com binary search, O(log n) time and O(1) space
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1

        while l<=r:
            m = (l+r)//2

            if ord(letters[m]) > ord(target):
                r = m - 1
            else:
                l = m + 1
        
        if l==len(letters):
            return letters[0]
        else:
            return letters[l]

