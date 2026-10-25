class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            unico = True
            for j in range(len(s)):
                if s[i] == s[j] and i != j:
                    unico = False
                    break
            if unico:
                return i
        return -1

