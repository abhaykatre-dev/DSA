class Solution:
    def countAndSay(self, n: int) -> str:
        ans="1"
        for _ in range(n-1):
            temp=""
            i=0
            while i<len(ans):
                j=i
                while j<len(ans) and ans[i]==ans[j]:
                    j+=1
                temp+=str(j-i)+ans[i]
                i=j
            ans=temp
        return ans        

                    
