# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def traverse(node, depth):
            if not node.left and not node.right:
                return depth

            ld, rd = 0, 0
            if node.left:
                ld = traverse(node.left, depth+1)
            if node.right:
                rd = traverse(node.right, depth+1)
            return max(ld, rd)
        
        return traverse(root, 1)
