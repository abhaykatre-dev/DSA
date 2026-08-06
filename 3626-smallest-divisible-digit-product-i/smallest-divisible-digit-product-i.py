class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while True:
            pro=1
            for digit in str(n):
                pro*=int(digit)
            if pro%t==0:
                return n
            n+=1
