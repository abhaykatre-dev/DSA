class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                index=i*n+j
                new_index=(index+k)%(m*n)
                row=new_index//n
                col=new_index%n
                ans[row][col]=grid[i][j]
        return ans
        # for _ in range(k):
        #     ans = [[0] * n for _ in range(m)]
        #     for i in range(m):
        #         for j in range(n):
        #             if i < m - 1 and j == n - 1:
        #                 ans[i + 1][0] = grid[i][j]
        #             elif i == m - 1 and j == n - 1:
        #                 ans[0][0] = grid[i][j]
        #             else:
        #                 ans[i][j + 1] = grid[i][j]
        #     grid = ans
        # return grid
