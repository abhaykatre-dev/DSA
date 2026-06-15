# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def func(node,level):
            if node is None:
                return 
            if len(ans)==level:
                ans.append(node.val)
            func(node.right,level+1)
            func(node.left,level+1)
        func(root,0)
        return ans

# from collections import deque
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None:
#             return []
#         queue=deque([root])
#         result=[]
#         while queue:
#             level_size=len(queue)
#             for i in range(level_size):
#                 node=queue.popleft()
#                 if i==level_size-1:
#                     result.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return result
        