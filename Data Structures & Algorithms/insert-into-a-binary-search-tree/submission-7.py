# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        parent = None
        curr = root

        while curr:
            if curr.val < val:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left
        
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        
        return root