from collections import deque
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for u,v in invocations:
            graph[u].append(v)
        suspicious=[False]*n
        suspicious[k]=True
        queue=deque()
        queue.append(k)
        while queue:
            u=queue.popleft()
            for v in graph[u]:
                if not suspicious[v]:
                    queue.append(v)
                    suspicious[v]=True
        for u,v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
        return [i for i in range(n) if not suspicious[i]]
        