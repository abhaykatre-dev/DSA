from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row=len(mat)
        col=len(mat[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        distance=[[0 for _ in range(col)] for _ in range(row)]
        queue=deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    queue.append([i,j,0])
                    visited[i][j]=1
        while queue:
            i,j,d=queue.popleft()
            distance[i][j]=d
            for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                new_i=i+dx
                new_j=j+dy
                if 0 <= new_i < row and 0 <= new_j < col and visited[new_i][new_j]==0:
                    visited[new_i][new_j]=1
                    queue.append([new_i,new_j,d+1])
        return distance