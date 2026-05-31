class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #TC - O(N.N!)
        result=[]
        used=[False]*len(nums)

        def backTrack(path):
            if len(path)==len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                path.append(nums[i])
                backTrack(path)
                path.pop()
                used[i]=False
        backTrack([])
        return result

        # result=[]
        # def backTrack(path):
        #     if len(path)==len(nums):
        #         result.append(path[:])
        #         return
            
        #     for num in nums:
        #         if num in path:
        #             continue
        #         path.append(num)
        #         backTrack(path)
        #         path.pop()
        # backTrack([])
        # return result    