"""
# Solução bruteforce: O(n) time space O(1)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        for i in range(n+1):
            if guess(i) == 0:
                return i
"""

# Solucao utilizando time O(log n) e space O(1) usando binary search
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n

        while l<=r:
            m = (l+r)//2

            if guess(m) == 0:
                return m
            elif guess(m) == -1:
                r = m - 1
            else:
                l = m + 1
            
        