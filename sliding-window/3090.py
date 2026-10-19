class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        melhor = 0

        hm = {}
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r],0)+1

            while hm[s[r]] > 2:
                hm[s[l]] -= 1
                l+=1
            
            melhor = max(melhor,r-l+1)

        return melhor