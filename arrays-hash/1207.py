class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hm = {}

        for n in arr:
            hm[n] = hm.get(n,0)+1

        seen = set()
        for key,value in hm.items():
            if value in seen:
                return False
            else:
                seen.add(value)
        
        return True