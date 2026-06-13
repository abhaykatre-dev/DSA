# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
#         def func(Node):
#             if Node is None:
#                 return 0
#             leftSum=func(Node.left)
#             rightSum=func(Node.right)
#             return 1+max(leftSum,rightSum)
#         return func(root)
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Iterative DFS Using Stack
        if root is None:
            return 0
        queue=deque([root])
        height=0
        while queue:
            level_height=len(queue)
            height+=1
            for _ in range(level_height):
                Node=queue.popleft()
                if Node.left is not None:
                    queue.append(Node.left)
                if Node.right is not None:
                    queue.append(Node.right)
        return height

       
      
        
            