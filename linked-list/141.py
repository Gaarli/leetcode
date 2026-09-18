"""
# Solução usando hashset O(n) time e O(n) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hs = set()

        curr = head
        while curr:
            if curr in hs:
                return True
            else:
                hs.add(curr)
            curr = curr.next
        return False

"""

# Solução usando 2 ponteiros O(n) time e O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# A ideia é que uma hora os ponteiros vão se encontrar
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # Se atentar na velocidade relativa
        # Como é 2-1, então e como se um tivesse parado
        # E o outro vai andando 1 por 1 (verificação)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                return True

        return False