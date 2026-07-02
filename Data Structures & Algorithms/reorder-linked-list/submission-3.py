# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        left = head
        right = left.next

        while right and right.next:
            left = left.next
            right = right.next.next

        middle = left
        prev = None

        # reverse the second half list
        while middle:
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp

        # bounce back and forth between first list and second
        left, right = head, prev
        while left and right:
            tmp = left.next
            left.next = right
            tmp2 = right.next
            right.next = tmp
            left = tmp
            right = tmp2
       