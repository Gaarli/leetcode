class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set('abcdefghijklmnopqrstuvwxyz')

        # Time O(26 * n) = O(n)
        # Space O(26) = O(1)
        for key in alphabet:
            if key not in sentence:
                return False
        
        return True