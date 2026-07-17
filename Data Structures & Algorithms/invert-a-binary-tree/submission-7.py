# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left and node.right:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                queue.append(node.left)
                queue.append(node.right)
            elif node.left:
                node.right = node.left
                node.left = None
                queue.append(node.right)
            elif node.right:
                node.left = node.right
                node.right = None
                queue.append(node.left)

        
        return root