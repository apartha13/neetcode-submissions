# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        res = False

        def isSame(p, q):
            if not p and not q:
                return True
            elif (not p and q) or (not q and p):
                return False
            elif p.val != q.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                res = isSame(node, subRoot)
                if res:
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return res

