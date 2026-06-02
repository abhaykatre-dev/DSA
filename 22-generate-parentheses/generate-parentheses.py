class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        s=['']*2*n
        def func(index,total):
            if index==len(s):
                if total==0:
                    result.append("".join(s))
                return
            if total<0 or total>n:
                return
            
            s[index]='('
            func(index+1,total+1)
            s[index]=')'
            func(index+1,total-1)
        func(0,0)
        return result