class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        left=0
        ans=[]
        for num in nums:
            total-=num     #right sum
            ans.append(abs(total-left))
            left+=num 
        return ans
        # n=len(nums)
        # leftsum=[0]*n
        # rightsum=[0]*n
        # for i in range(1,n):
        #     leftsum[i]=leftsum[i-1]+nums[i-1]
        # for j in range(n-2,-1,-1):
        #     rightsum[j]=rightsum[j+1]+nums[j+1]
        
        # ans=[0]*n
        # for i in range(n):
        #     ans[i]=abs(leftsum[i]-rightsum[i])
        # return ans
            