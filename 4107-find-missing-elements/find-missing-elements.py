class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest,largest=float('inf'),float('-inf')
        for num in nums:
            smallest=min(smallest,num)
            largest=max(largest,num)
        ans=[]
        myset=set(nums)
        for num in range(smallest+1,largest):
            if num not in myset:
                ans.append(num)
        return ans