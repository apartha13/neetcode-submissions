"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        if not node:
            return None
    
        q = deque()
        q.append(node)
        clone[node.val] = Node(node.val)

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei.val not in clone:
                    clone[nei.val] = Node(nei.val)
                    q.append(nei)
                clone[curr.val].neighbors.append(clone[nei.val])
        
        return clone[node.val]

