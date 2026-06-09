class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #better
        maxi=0
        zeros=0
        left=0
        right=0
        n=len(nums)
        while right<n:
            if nums[right]==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            if zeros<=k:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi
        # bruteforce
        # maxi=0
        # n=len(nums)
        # for i in range(n):
        #     zeros=0
        #     for j in range(i,n):
        #         if nums[j]==0:
        #             zeros+=1
        #         if zeros>k:
        #             break
        #         maxi=max(maxi,j-i+1)
        # return maxi