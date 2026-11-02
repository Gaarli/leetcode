class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        hm2 = {}

        for c in chars:
            hm2[c] = hm2.get(c,0)+1

        count = 0
        for w in words:
            hm1 = {}

            for j in range(len(w)):
                hm1[w[j]] = hm1.get(w[j],0)+1
            
            flag = True
            
            for key,value in hm1.items():
                if value > hm2.get(key,0):
                    flag = False
                    break
            
            if flag:
                count+=len(w)
            
        return count