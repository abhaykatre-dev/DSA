class Solution:
    def validStrings(self, n: int) -> List[str]:
        result=[]
        s=['0']*n
        def fun(index,prev_zero):
            if index==n:
                result.append("".join(s))
                return

            s[index]='1'
            fun(index+1,False)
            
            if not prev_zero:
                s[index]='0'
                fun(index+1,True) 

        fun(0,False)
        return result