class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        # Brute force approach (O(n^2) time and O(1) space)
        """for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == 2*arr[j] and i!=j:
                    return True

        return False
        """

        # Hashing approach (O(n) time and O(n) space)
        seen = set()

        for i in range(len(arr)):
            if 2*arr[i] in seen or (arr[i]%2==0 and arr[i]/2 in seen):
                return True
            if arr[i] not in seen:
                seen.add(arr[i])

        return False 