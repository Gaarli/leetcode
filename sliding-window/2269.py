# Solução O(n) time and O(1) space usando sliding window
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l = 0
        r = k-1

        count = 0
        strnum = str(num)

        while r < len(strnum):
            seq = int(strnum[l:r+1])
            if seq != 0 and num % seq == 0:
                count += 1

            l+=1
            r+=1
        
        return count