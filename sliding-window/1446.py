class Solution:
    def maxPower(self, s: str) -> int:
        melhor = 0
        l = 0

        for r in range(len(s)):
            while s[l] != s[r]:
                l+=1

            melhor = max(melhor,r-l+1)

        return melhor