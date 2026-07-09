class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp=[0]*n
        for i in range(1,n):
            if abs(nums[i]-nums[i-1])<=maxDiff:
                comp[i]=comp[i-1]
            else:
                comp[i]=i
        res=[]
        for u,v in queries:
            if comp[u]==comp[v]:
                res.append(True)
            else:
                res.append(False)
        return res