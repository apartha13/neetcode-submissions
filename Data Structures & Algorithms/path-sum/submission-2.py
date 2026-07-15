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
        
        queue = deque()
        queue.append((root, targetSum))

        while queue:
            qLen = len(queue)

            for _ in range(qLen):
                node, rSum = queue.popleft()
                rSum -= node.val

                if rSum == 0 and not node.left and not node.right:
                    return True
                
                if node.left:
                    queue.append((node.left, rSum))
                if node.right:
                    queue.append((node.right, rSum))
        
        return False
