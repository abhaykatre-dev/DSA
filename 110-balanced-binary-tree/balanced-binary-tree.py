# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if node is None:
                return 0
            LH=balanced(node.left)
            if LH==-1:
                return -1
            RH=balanced(node.right)
            if RH==-1:
                return -1
            if abs(LH-RH)>1:
                return -1
            return 1+max(LH,RH)
        return balanced(root)!=-1