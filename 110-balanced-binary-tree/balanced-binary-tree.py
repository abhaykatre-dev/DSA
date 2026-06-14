# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def func(node):
            if node is None:
                return 0
            LH=func(node.left)
            if LH==-1:
                return -1
            RH=func(node.right)
            if RH==-1:
                return -1
            if abs(LH-RH)>1:
                return -1
            return 1+max(LH,RH)
        return func(root)!=-1

        return func(root,True)