class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        #estrategia é contar substrings pela
        # soma de substrings q terminam em s[r]

        l = 0
        melhor = 0 # Contador de substrings
        zeros=0
        ones=0
        for r in range(len(s)):
            if s[r] == '0':
                zeros+=1
            else:
                ones+=1
            
            while ones>k and zeros>k:
                if s[l]=='0':
                    zeros-=1
                else:
                    ones-=1
                l+=1
            
            melhor = melhor + r-l+1

        return melhor

