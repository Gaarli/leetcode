# Time O(n) e space O(n)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slist = list(s)
        for l in range(0,len(s),2*k):
            if len(s)-1 - l + 1 < k:
                r = len(s)-1
            else:
                r = l + k - 1

            while l<r:
                slist[l],slist[r]=slist[r],slist[l]
                l+=1
                r-=1
            
        return "".join(slist)