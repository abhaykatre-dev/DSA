class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        jump=0
        left=0
        right=0
        while right<n-1:
            farthest=0
            for i in range(left,right+1):
                farthest=max(farthest,i+nums[i])
            left=right+1
            right=farthest
            jump+=1
        return jump

        # n = len(nums)
        # def func(idx, jump):
        #     if idx >= n - 1:
        #         return jump

        #     min_jump = float('inf')

        #     for i in range(1, nums[idx] + 1):
        #         min_jump = min(min_jump, func(idx + i, jump + 1))

        #     return min_jump
        # return func(0, 0)