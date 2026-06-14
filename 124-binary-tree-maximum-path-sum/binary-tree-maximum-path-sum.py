# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        def func(node):
            if node is None:
                return 0
            leftsum=func(node.left)
            if leftsum<0:
                leftsum=0
            rightsum=func(node.right)
            if rightsum<0:
                rightsum=0
            self.maxi=max(self.maxi,leftsum+node.val+rightsum)
            return node.val+max(leftsum,rightsum)
        func(root)
        return self.maxi

            