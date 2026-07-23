# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        start = head
        end = prev
        while start and end and start != end:
            tmp1 = start.next
            start.next = end
            start = tmp1
            tmp2 = end.next
            end.next = start
            end = tmp2


