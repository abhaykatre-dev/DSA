class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        # numbers are in the range [1, n].
        # use the value as an index and mark the corresponding element negative.
        # if it's already negative, the number has appeared before.
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                ans.append(abs(num))
            else:
                nums[index] = -nums[index]
        return ans