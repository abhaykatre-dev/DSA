class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot=-1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        if pivot==-1:
            self.reverse(nums,0,n-1)
            return
        for i in range(n-1,pivot,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        self.reverse(nums,pivot+1,n-1)

    def reverse(self,nums,st,end):
        while st<end:
            nums[st],nums[end]=nums[end],nums[st]
            st+=1
            end-=1

