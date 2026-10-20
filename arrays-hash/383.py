class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm1 = {}

        for i in range(len(ransomNote)):
            hm1[ransomNote[i]] = hm1.get(ransomNote[i],0)+1

        hm2 = {}

        for j in range(len(magazine)):
            if magazine[j] in hm1: # O(1) lookup
                hm2[magazine[j]] = hm2.get(magazine[j],0)+1
            
        for key,value in hm1.items():
            if key not in hm2 or value > hm2[key]:
                return False
        
        return True