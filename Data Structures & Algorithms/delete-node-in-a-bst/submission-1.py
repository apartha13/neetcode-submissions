# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        parent = None
        curr = root

        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        if not curr:
            return root
        
        if not curr.left and not curr.right:
            if not parent:
                return None
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        
        elif not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if not parent:
                return child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        
        else:
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            
            curr.val = succ.val

            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
        
        return root