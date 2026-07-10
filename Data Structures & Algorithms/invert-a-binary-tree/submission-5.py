# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return
            
            if root.right and root.left:
                tmp = root.right
                root.right = root.left
                root.left = tmp
                dfs(root.left)
                dfs(root.right)
            elif root.right:
                root.left = root.right
                root.right = None
                dfs(root.left)
            elif root.left:
                root.right = root.left
                root.left = None
                dfs(root.right)
            
            return
        
        dfs(root)
        return root
            
