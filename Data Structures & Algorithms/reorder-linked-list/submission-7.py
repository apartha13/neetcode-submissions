# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        secondEnd = slow.next
        mid.next = None
        prev = None
        while secondEnd:
            tmp = secondEnd.next
            secondEnd.next = prev
            prev = secondEnd
            secondEnd = tmp
        
        end = prev
        start = head
        while start and end:
            tmp1 = start.next
            start.next = end
            start = tmp1
            tmp2 = end.next
            end.next = start
            end = tmp2
        




