# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res
            
        q = deque([])
        q.append((root, 1))
        arr = []
        curr = 1

        while q:
            node, level = q.popleft()

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            
            if level != curr:
                res.append(arr)
                curr += 1
                arr = []

            arr.append(node.val)

        if arr:
            res.append(arr)

        return res


                
