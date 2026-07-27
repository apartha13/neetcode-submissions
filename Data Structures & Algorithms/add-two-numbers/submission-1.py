# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output1 = ""
        output2 = ""

        while l1 or l2:
            if l1:
                output1 = str(l1.val) + output1
                l1 = l1.next
            if l2:
                output2 = str(l2.val) + output2
                l2 = l2.next
        
        total = str(int(output1) + int(output2))
        root = ListNode(int(total[-1]))

        prev = root
        for i in range(len(total) - 2, -1, -1):
            curr = ListNode(int(total[i]))
            prev.next = curr
            prev = curr
        
        return root
        