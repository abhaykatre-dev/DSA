class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans=0
        myset=set()
        for num in nums:
            if num not in myset:
                myset.add(num)
            else:
                ans=ans^num
        return ans