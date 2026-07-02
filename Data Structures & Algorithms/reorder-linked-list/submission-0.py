# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # reorder the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        top, end = head, prev
        # bounce back and forth between LL
        while end:
            tmp1, tmp2 = top.next, end.next
            top.next = end
            end.next = tmp1
            top = tmp1
            end = tmp2
        