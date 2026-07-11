class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        visited=[False]*n
        def dfs(node,comp):
            visited[node]=True
            comp.append(node)
            for adjnode in adj_list[node]:
                if not visited[adjnode]:
                    dfs(adjnode,comp)

        ans=0
        for i in range(n):
            comp=[]
            if not visited[i]:
                dfs(i,comp)
                nodes=len(comp)
                edge_count=0
                for node in comp:
                    edge_count+=len(adj_list[node])
                # Each node count twice as it is undirected graph  
                edge_count//=2
                # In complete connected componet there are n*(n-1)/2 edges are there where n is no. of vertices
                if edge_count==nodes*(nodes-1)//2:
                    ans+=1
        return ans


        return cnt