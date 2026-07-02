# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ curr, nxt = head, head

        while nxt and nxt.next:
            curr = curr.next
            nxt = nxt.next.next
            if curr == nxt:
                return True
            
        return False """
        mySet = set()
        curr = head
        while curr:
            if curr not in mySet:
                mySet.add(curr)
            else:
                return True
            curr = curr.next
        return False
