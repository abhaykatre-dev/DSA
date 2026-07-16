class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=[]
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        prefixGcd=[]
        maxi=0
        for num in nums:
            maxi=max(num,maxi)
            prefixGcd.append(gcd(num,maxi))
        prefixGcd.sort()
        l,r=0,len(prefixGcd)-1
        ans=0
        while l<r:
            ans+=gcd(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1
        return ans
            
