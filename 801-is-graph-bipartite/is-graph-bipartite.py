class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        total_nodes=len(graph)
        visited=[-1]*total_nodes
        for i in range(total_nodes):
            if visited[i]==-1:
                ans=self.dfs(i,visited,graph,0)
                if ans==False:
                    return False
        return True
    
    def dfs(self,current_node,visited,graph,color):
        visited[current_node]=color
        for adjNode in graph[current_node]:
            if visited[adjNode]!=-1:
                if visited[adjNode]==color:
                    return False
            else:
                ans=self.dfs(adjNode,visited,graph,1-color)
                if ans==False:
                    return False
        return True

