# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        res = []
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
        
            if node.left and node.right:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                q.append(node.left)
                q.append(node.right)
            elif node.left:
                node.right = node.left
                node.left = None
                q.append(node.right)
            elif node.right:
                node.left = node.right
                node.right = None
                q.append(node.left)
        
        return root