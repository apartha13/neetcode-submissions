# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        i = 0 

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                i += 1
                root = stack.pop()
                if i == k:
                    return root.val
                root = root.right
        
        return 0
