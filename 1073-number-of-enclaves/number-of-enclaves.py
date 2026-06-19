class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row=len(grid)
        col=len(grid[0])
        def dfs(r,c):
            if 0<=r<row and 0<=c<col:
                if grid[r][c]==1:
                    grid[r][c]='X'
                    dfs(r+1,c)
                    dfs(r-1,c)
                    dfs(r,c+1)
                    dfs(r,c-1)
        #top and bottom
        for i in range(col):
            if grid[0][i]==1:
                dfs(0,i)
            if grid[row-1][i]==1:
                dfs(row-1,i)
        #left and right
        for i in range(row):
            if grid[i][0]==1:
                dfs(i,0)
            if grid[i][col-1]==1:
                dfs(i,col-1)
        move=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    move+=1
        return move
        