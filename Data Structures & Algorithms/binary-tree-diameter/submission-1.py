# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maxDepth = 0

        def dfs(node):
            if not node:
                return 0
            
            left_depth, right_depth = dfs(node.left), dfs(node.right)

            self.maxDepth = max(self.maxDepth, left_depth + right_depth)
            
            return 1 + max(left_depth, right_depth)
        
        dfs(root)

        return self.maxDepth
        