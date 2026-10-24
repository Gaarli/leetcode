class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        f = {}
        finv = {}

        for i in range(len(s)):
            x = s[i]
            y = t[i]

            if x in f and f[x] != y:
                return False
            
            if y in finv and finv[y] != x:
                return False
            
            f[x] = y
            finv[y] = x
        
        return True

        return True