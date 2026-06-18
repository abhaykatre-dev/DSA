from copy import deepcopy
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #  using queue
        if image[sr][sc]==color:
            return image
        row=len(image)
        col=len(image[0])
        visited=deepcopy(image)
        intial_color=visited[sr][sc]
        queue=deque()
        queue.append([sr,sc])
        while queue:
            i,j=queue.popleft()
            visited[i][j]=color
            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                new_i=i+x
                new_j=j+y
                if new_i<0 or new_i==row or new_j<0 or new_j==col:
                    continue
                if visited[new_i][new_j]!=intial_color:
                    continue
                queue.append([new_i,new_j])
        return visited


        # using bfs
#         if image[sr][sc]==color:
#             return image
#         row=len(image)
#         col=len(image[0])
#         visited=deepcopy(image)
#         intialcolor=image[sr][sc]
#         def func(i,j):
#             if i<0 or i==row or j<0 or j==col:
#                 return
#             if visited[i][j]!=intialcolor:
#                 return
#             if visited[i][j]==color:
#                 return
#             visited[i][j]=color
#             func(i+1,j)
#             func(i-1,j)
#             func(i,j+1)
#             func(i,j-1)
#         func(sr,sc)
#         return visited