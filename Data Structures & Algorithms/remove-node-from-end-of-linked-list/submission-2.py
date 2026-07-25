# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
            
        curr = head
        node = 1
        
        while curr.next:
            curr = curr.next
            node += 1
        
        delIndex = node - n
        
        dummy = prev = ListNode(0, head)
        trav = head
        ind = 0

        while ind != delIndex:
            prev = trav
            trav = trav.next
            ind += 1
        
        prev.next = trav.next
        return dummy.next