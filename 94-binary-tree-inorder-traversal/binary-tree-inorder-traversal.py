# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result=[]
        self.inorder(root)
        return self.result

        
    def inorder(self,Node):
        if not Node:#Node is None 
            return
        self.inorder(Node.left)
        self.result.append(Node.val)
        self.inorder(Node.right)