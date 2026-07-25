class Solution:
    def maxProduct(self, n: int) -> int:
        # res=[]
        # for ch in str(n):
        #     res.append(int(ch))
        # res.sort()
        # return res[-1]*res[-2]
        # n=str(n)
        # ans=0
        # for i in range(len(n)-1):
        #     for j in range(i+1,len(n)):
        #         ans=max(ans,int(n[i])*int(n[j]))
        # return ans
        n=str(n)
        largest=float('-inf')
        s_largest=float('-inf')
        for ch in n:
            num=int(ch)
            if num>=largest:
                s_largest=largest
                largest=num
            elif largest>num>s_largest:
                s_largest=num

        return largest*s_largest
            


