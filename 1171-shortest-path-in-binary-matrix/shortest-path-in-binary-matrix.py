class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid)-1]==1:
            return -1
        row=len(grid)
        col=len(grid)
        distance=[[float('inf') for _ in range(col)] for _ in range(row)]
        distance[0][0]=1
        queue=deque()
        queue.append((1,0,0))
        while queue:
            dist,i,j=queue.popleft()
            for x,y in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
                new_i,new_j=i+x,j+y
                if new_i==row or new_i<0 or new_j==col or new_j<0:
                    continue
                if grid[new_i][new_j]==1:
                    continue
                if dist+1<distance[new_i][new_j]:
                    if new_i==row-1 and new_j==col-1:
                        return dist+1
                    distance[new_i][new_j]=dist+1
                    queue.append((dist+1,new_i,new_j))
        if distance[row-1][col-1]==float('inf'):
            return -1
        return distance[row-1][col-1]