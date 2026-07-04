class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustscore=[0]*(n+1)
        for a,b in trust:
            trustscore[a]-=1
            trustscore[b]+=1
        for i in range(1,n+1):
            if trustscore[i]==n-1:
                return i
        return -1    