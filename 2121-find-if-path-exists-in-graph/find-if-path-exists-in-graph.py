class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        adj_list=[[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        queue=deque()
        queue.append(source)
        visited={source}
        while queue:
            node=queue.popleft()
            for adjnode in adj_list[node]:
                if adjnode==destination:
                    return True
                if adjnode not in visited:
                    visited.add(adjnode)
                    queue.append(adjnode)

        return False