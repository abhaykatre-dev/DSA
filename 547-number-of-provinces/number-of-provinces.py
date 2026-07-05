class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[0]*n
        province=0
        def dfs(city):
            visited[city]=1
            for nei in range(n):
                if isConnected[city][nei]==1 and visited[nei]==0:
                    dfs(nei)

        for i in range(n):
            if visited[i]==0:
                province+=1
                dfs(i)
        return province