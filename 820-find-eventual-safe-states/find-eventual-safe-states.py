class Solution:
    def dfs(self,curr_node,visited,path_visited,is_safe,adj_list):
        visited[curr_node]=1
        path_visited[curr_node]=1
        for adjnode in adj_list[curr_node]:
            if visited[adjnode]==0:
                if self.dfs(adjnode,visited,path_visited,is_safe,adj_list)==False:
                    return False
            elif path_visited[adjnode]==1:
                return False
        is_safe[curr_node]=1
        path_visited[curr_node]=0
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=len(graph)
        visited=[0]*V
        path_visited=[0]*V
        is_safe=[0]*V

        for i in range(V):
            if visited[i]==0:
                self.dfs(i,visited,path_visited,is_safe,graph)
        
        result=[]
        for i in range(V):
            if is_safe[i]==1:
                result.append(i)
        return result


        # V=len(graph)
        # adj_list=[[] for _ in range(V)]
        # inDegree=[0 for _ in range(V)]
        # for node in range(V):
        #     for adjnode in graph[node]:
        #         adj_list[adjnode].append(node)
        #         inDegree[node]+=1
        # queue=deque()
        # for node in range(V):
        #     if inDegree[node]==0:
        #         queue.append(node)
        # result=[]
        # while queue:
        #     curr_node=queue.popleft()
        #     for adjnode in adj_list[curr_node]:
        #         inDegree[adjnode]-=1
        #         if inDegree[adjnode]==0:
        #             queue.append(adjnode)
        #     result.append(curr_node)
        # result.sort()
        # return result
