class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        frase = s.split()

        if len(pattern) != len(frase):
            return False

        f = {}
        finv = {}

        for i in range(len(pattern)):
            if pattern[i] in f and f[pattern[i]] != frase[i]:
                return False
            
            if frase[i] in finv and finv[frase[i]] != pattern[i]:
                return False

            f[pattern[i]] = frase[i]
            finv[frase[i]] = pattern[i]

        return True