class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V=len(graph)
        adj_list=[[] for _ in range(V)]
        inDegree=[0 for _ in range(V)]
        for node in range(V):
            for adjnode in graph[node]:
                adj_list[adjnode].append(node)
                inDegree[node]+=1
        queue=deque()
        for node in range(V):
            if inDegree[node]==0:
                queue.append(node)
        result=[]
        while queue:
            curr_node=queue.popleft()
            for adjnode in adj_list[curr_node]:
                inDegree[adjnode]-=1
                if inDegree[adjnode]==0:
                    queue.append(adjnode)
            result.append(curr_node)
        result.sort()
        return result
