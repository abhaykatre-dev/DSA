class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        ans=-1
        for num in arr:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]==num:
                ans=max(ans,num)
        return ans