# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
            
        def dfs(node, tot):
            tot -= node.val
            if tot == 0 and not node.left and not node.right:
                return True
            
            left, right = False, False
            
            if node.left:
                left = dfs(node.left, tot)
            if node.right:
                right = dfs(node.right, tot)
            
            return left or right
        
        return dfs(root, targetSum)
            