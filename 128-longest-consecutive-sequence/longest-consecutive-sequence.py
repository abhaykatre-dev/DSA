class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset=set(nums)
        longest=0
        for num in myset:
            if num-1 not in myset:
                x=num
                cnt=1
                while x+1 in myset:
                    cnt+=1
                    x+=1
                longest=max(longest,cnt)

        return longest