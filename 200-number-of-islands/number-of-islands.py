class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row=len(grid)
        col=len(grid[0])
        ans=0
        queue=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    grid[i][j]='0'
                    queue.append((i,j))
                    while queue:
                        c,r=queue.popleft()
                        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            new_i,new_j=c+dx,r+dy
                            if new_i<0 or new_i==row or new_j<0 or new_j==col:
                                continue
                            if grid[new_i][new_j]=="0":
                                continue
                            grid[new_i][new_j]="0"
                            queue.append((new_i, new_j))
                    ans+=1
        return ans
        

        # row=len(grid)
        # col=len(grid[0])
        # total_islands=0
        # def dfs(i,j):
        #     if i<0 or i==row or j<0 or j==col:
        #         return
        #     if grid[i][j]=='0':
        #         return
        #     grid[i][j]="0"
        #     dfs(i+1,j)
        #     dfs(i-1,j)
        #     dfs(i,j+1)
        #     dfs(i,j-1)
        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j]=="1":
        #             dfs(i,j)
        #             total_islands+=1
        # return total_islands