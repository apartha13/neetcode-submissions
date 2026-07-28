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
        
        l1 = head
        l2 = prev

        while l1 and l2 and l1 != l2:
            tmp1 = l1.next
            l1.next = l2
            l1 = tmp1
            tmp2 = l2.next
            l2.next = l1
            l2 = tmp2
        
