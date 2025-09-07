# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, curDepth):
            if not node:
                return curDepth - 1

            return max(traverse(node.left, curDepth+1), traverse(node.right, curDepth+1))
        
        return traverse(root, 1)
