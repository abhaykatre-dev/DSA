class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range(2*n-1,-1,-1):
            # [1,2,3,4,3,1,2,3,4,3]
            # To access index 9 -> 9 % 5 = 4
            # nums[4] = 3
            while stack and stack[-1]<=nums[i%n]: 
                stack.pop()
            if i<n and stack:
                ans[i]=stack[-1]
            stack.append(nums[i%n])
        return ans

           