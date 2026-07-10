# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        visit = set()
        q = deque()
        res = []

        q.append(root)

        while q:
            qLen = len(q)
            arr = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    arr.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            res.append(arr)
        
        return res