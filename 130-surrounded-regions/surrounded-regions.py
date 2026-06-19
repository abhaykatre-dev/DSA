from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row=len(board)
        col=len(board[0])
        visited=[[0]*col for _ in range(row)]
        def dfs(i,j):
            if i<0 or i==row or j<0 or j==col :
                return 
            if visited[i][j]==1 or board[i][j]=='X':
                return
            visited[i][j]=1
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        #top border
        for i in range(0,col):
            if board[0][i]=='O':
                if visited[0][i]==0:
                    dfs(0,i)
        #right border
        for i in range(0,row):
            if board[i][col-1]=='O':
                if visited[i][col-1]==0:
                    dfs(i,col-1)
        #bottom border
        for i in range(0,col):
            if board[row-1][i]=='O':
                if visited[row-1][i]==0:
                    dfs(row-1,i)
        #left border
        for i in range(0,row):
            if board[i][0]=='O':
                 if visited[i][0]==0:
                    dfs(i,0)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and visited[i][j]==0:
                    board[i][j]='X'
        