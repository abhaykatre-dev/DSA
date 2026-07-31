# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def func(node):
            if not node:
                return 0
            if not node.left:
                return 1+func(node.right)
            if not node.right:
                return 1+func(node.left)
            LH=func(node.left)
            RH=func(node.right)
            return 1+min(LH,RH)
        return func(root)