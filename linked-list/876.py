"""
# Brute force usando O(n) time e O(n) space com um array auxiliar que guarda os nós da linked-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        res = []
        while curr:
            res.append(curr)
            curr = curr.next
        
        return res[len(res)//2]

"""


# Solução com time O(n) e space O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        curr = head
        n = 0
        m = count//2

        while curr:
            if n == m:
                return curr
            n+=1
            curr = curr.next