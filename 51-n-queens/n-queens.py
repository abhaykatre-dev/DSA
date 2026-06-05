class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=['.'*n for _ in range(n)]
        result=[]
        left=[0]*n
        upper_diagonal=[0]*(2*n-1)
        lower_diagonal=[0]*(2*n-1)
        self.solve(0,board,result,left,upper_diagonal,lower_diagonal,n)
        return result
    
    def solve(self,col,board,result,left,upper_diagonal,lower_diagonal,n):
        if col==n:
            result.append(board[:])
            return
        for row in range(n):
            if left[row]==0 and upper_diagonal[n-1+col-row]==0 and lower_diagonal[row+col]==0:
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                left[row]=1
                upper_diagonal[n-1+col-row]=1
                lower_diagonal[row+col]=1
                self.solve(col+1,board,result,left,upper_diagonal,lower_diagonal,n)
                board[row]=board[row][:col]+'.'+board[row][col+1:]
                left[row]=0
                upper_diagonal[n-1+col-row]=0
                lower_diagonal[row+col]=0


    #bruteForce
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     board=['.'*n for _ in range(n)]
    #     result=[]
    #     self.solve(0,board,result,n)
    #     return result
    
    # def solve(self,col,board,result,n):
    #     if col==n:
    #         result.append(list(board))
    #         return
    #     for row in range(n):
    #         if self.isCorrectPosition(row,col,board,n):
    #             board[row]=board[row][:col]+'Q'+board[row][col+1:]
    #             self.solve(col+1,board,result,n)
    #             board[row]=board[row][:col]+'.'+board[row][col+1:]
    
    # def isCorrectPosition(self,row,col,board,n):
    #     tempRow=row
    #     tempCol=col
    #     #Diagonally
    #     while tempRow>=0 and tempCol>=0:
    #         if board[tempRow][tempCol]=='Q':
    #             return False
    #         tempRow-=1
    #         tempCol-=1
    #     #Check left row
    #     tempRow=row
    #     tempCol=col
    #     while tempCol>=0:
    #         if board[tempRow][tempCol]=='Q':
    #             return False
    #         tempCol-=1
    #     #check lower diagonal toward left
    #     tempRow=row
    #     tempCol=col
    #     while tempRow<n and tempCol>=0:
    #         if board[tempRow][tempCol]=='Q':
    #             return False
    #         tempRow+=1
    #         tempCol-=1
    #     return True