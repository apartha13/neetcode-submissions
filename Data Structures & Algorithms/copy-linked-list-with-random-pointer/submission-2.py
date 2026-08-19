"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        copy = {None: None}
        curr = head 

        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        
        trav = head
        while trav: 
            copy[trav].next = copy[trav.next] 
            copy[trav].random = copy[trav.random]
            trav = trav.next
        
        return copy[head]
