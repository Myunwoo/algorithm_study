class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )

        return isMirror(root.left, root.right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(left, right):
            if left and right and left.val == right.val:
                return traverse(left.left, right.right) and traverse(left.right, right.left)
            elif not left and not right:
                return True
            else:
                return False

                    
        return traverse(root.left, root.right)