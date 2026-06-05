class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #bruteForce
        board=['.'*n for _ in range(n)]
        result=[]
        self.solve(0,board,result,n)
        return result
    
    def solve(self,col,board,result,n):
        if col==n:
            result.append(list(board))
            return
        for row in range(n):
            if self.isCorrectPosition(row,col,board,n):
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                self.solve(col+1,board,result,n)
                board[row]=board[row][:col]+'.'+board[row][col+1:]
    
    def isCorrectPosition(self,row,col,board,n):
        tempRow=row
        tempCol=col
        #Diagonally
        while tempRow>=0 and tempCol>=0:
            if board[tempRow][tempCol]=='Q':
                return False
            tempRow-=1
            tempCol-=1
        #Check left row
        tempRow=row
        tempCol=col
        while tempCol>=0:
            if board[tempRow][tempCol]=='Q':
                return False
            tempCol-=1
        #check lower diagonal toward left
        tempRow=row
        tempCol=col
        while tempRow<n and tempCol>=0:
            if board[tempRow][tempCol]=='Q':
                return False
            tempRow+=1
            tempCol-=1
        return True