class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #bfs
        if not grid:
            return 0
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        #top and bottom
        for i in range(col):
            if grid[0][i]==1:
                queue.append((0,i))
            if grid[row-1][i]==1:
                queue.append((row-1,i))
        #left and right
        for i in range(row):
            if grid[i][0]==1:
                queue.append((i,0))
            if grid[i][col-1]==1:
                queue.append((i,col-1))
        while queue:
            i,j=queue.popleft()
            grid[i][j]=0
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_i=i+dx
                new_j=j+dy
                if new_i<0 or new_i>=row or new_j<0 or new_j>=col:
                    continue
                if grid[new_i][new_j]!=1:
                    continue
                grid[new_i][new_j]=0
                queue.append((new_i,new_j))
        move=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    move+=1
        return move


        #dfs
        # if not grid:
        #     return 0
        # row=len(grid)
        # col=len(grid[0])
        # def dfs(r,c):
        #     if r<0 or r>=row or c<0 or c>=col or grid[r][c]!=1:
        #         return 0
        #     grid[r][c]=0
        #     dfs(r+1,c)
        #     dfs(r-1,c)
        #     dfs(r,c+1)
        #     dfs(r,c-1)
        # #top and bottom
        # for i in range(col):
        #     if grid[0][i]==1:
        #         dfs(0,i)
        #     if grid[row-1][i]==1:
        #         dfs(row-1,i)
        # #left and right
        # for i in range(row):
        #     if grid[i][0]==1:
        #         dfs(i,0)
        #     if grid[i][col-1]==1:
        #         dfs(i,col-1)
        # move=0
        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j]==1:
        #             move+=1
        # return move
        