# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 배열을 반으로 나누고
        # 가운데 인덱스는 루트로 삼고
        # 양쪽 배열에 대해 같은 동작을 수행하는데,
        # 재귀 호출을 하면서 재귀 함수가 각자의 루트를 반환하고
        # 호출한 곳에서 그 루트를 left, right에 넣는다
        def makeTree(arr):
            rootVal = arr[len(arr)//2]
            lArr = arr[:len(arr)//2]
            rArr = arr[len(arr)//2+1:]

            node = TreeNode()
            node.val = rootVal

            if lArr:
                node.left = makeTree(lArr)
            if rArr:
                node.right = makeTree(rArr)
            return node
        
        return makeTree(nums)