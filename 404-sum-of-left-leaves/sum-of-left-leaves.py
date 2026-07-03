# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum=0
        def func(node,is_left):
            if node is None:
                return None
            if not node.left and not node.right and is_left:
                self.sum+=node.val
            func(node.left,True)
            func(node.right,False)
            
        func(root,False)
        return self.sum