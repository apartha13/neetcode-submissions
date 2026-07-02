# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidTree(left, root, right):
            if not root:
                return True
            elif left < root.val < right:
                return (isValidTree(left, root.left, root.val) and isValidTree(root.val, root.right, right))
            else:
                return False
        
        return isValidTree(float('-inf'), root, float('inf'))
