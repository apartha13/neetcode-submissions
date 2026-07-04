# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        later = head

        while later:
            tmp = later.next
            later.next = curr
            curr = later
            later = tmp
        
        return curr