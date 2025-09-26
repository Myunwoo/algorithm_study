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

        def countDepth(root, count):
            if not root.left and not root.right:
                return count
            l, r = 0, 0
            if root.left:
                l = countDepth(root.left, count+1)
            if root.right:
                r = countDepth(root.right, count+1)
            return max(l, r)
        
        def traverse(node, curDepth):
            if not node:
                return curDepth - 1

            return max(traverse(node.left, curDepth+1), traverse(node.right, curDepth+1))
        
        return countDepth(root, 1)