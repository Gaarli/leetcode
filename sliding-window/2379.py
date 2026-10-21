class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        melhor = k
        white = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                white+=1

            if r>=k and blocks[r-k]=='W':
                white-=1
            
            if r>=k-1:
                melhor = min(melhor,white)

        return melhor

"""Outra solução (usando hashmap, como é dois caracteres
ainda é O(2) = O(1) space)

```python3
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        melhor = k

        hm = {'B':0, 'W':0}
        for r in range(len(blocks)):
            hm[blocks[r]] = hm.get(blocks[r],0)+1

            if r>=k:
                hm[blocks[r-k]] -= 1
            
            if r>=k-1:
                melhor = min(melhor,hm['W'])

        return melhor
```

"""