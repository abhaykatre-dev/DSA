class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]==n//2:
                return num
        
