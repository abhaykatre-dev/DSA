class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        res=0
        while n>0:
            LD=n%10
            if LD!=0:
                res=res*10+LD
                sum+=LD
            n=n//10
        res=int(str(res)[::-1])
        return res*sum 
