class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        l = 0
        r = 0

        while word[r] != ch:
            r+=1
        
        strlist = list(word)

        while l<r:
            strlist[l],strlist[r]=strlist[r],strlist[l]
            l+=1
            r-=1

        return "".join(strlist)