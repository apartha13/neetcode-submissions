# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return []

        dummy = prev = ListNode(0, head)
        curr = head
        
        for _ in range(left - 1):
            prev, curr = curr, curr.next
        
        newPrev = None
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = newPrev
            newPrev, curr = curr, tmp
        
        prev.next.next = curr
        prev.next = newPrev

        return dummy.next