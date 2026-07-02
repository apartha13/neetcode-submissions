# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next
        
        targetNode = counter - n
        i = 0
        newCurr = head
        prev = None
        while newCurr:
            if i == targetNode:
                if i != 0:
                    prev.next = newCurr.next
                else:
                    head = newCurr.next
                return head
            i += 1
            prev = newCurr
            newCurr = newCurr.next
        return head