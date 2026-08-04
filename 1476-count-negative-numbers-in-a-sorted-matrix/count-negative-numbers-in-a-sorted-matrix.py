class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # cnt=0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j]<0:
        #             cnt+=1
        # return cnt
        
        rows=len(grid)
        cols=len(grid[0])
        i=rows-1 #starting from buttom
        j=0
        cnt=0
        while i>=0 and j<cols:
            if grid[i][j]<0:
                cnt+=cols-j
                i-=1
            else:
                j+=1
        return cnt