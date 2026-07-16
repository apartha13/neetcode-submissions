# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        large = max(p.val, q.val)
        small = min(p.val, q.val)

        curr = root

        while curr:
            if curr.val > large:
                curr = curr.left
            elif curr.val < small:
                curr = curr.right
            else:
                return curr
        
        return None