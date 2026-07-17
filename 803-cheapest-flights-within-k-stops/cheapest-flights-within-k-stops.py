from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list=[[] for i in range(n)]
        for u,v,d in flights:
            adj_list[u].append([v,d])
        min_cost=[float('inf') for i in range(n)]
        min_cost[src]=0
        queue=deque()
        queue.append([0,src,0])
        while queue:
            stops,city,cost = queue.popleft()
            for nxt,price in adj_list[city]:
                new_cost=cost+price
                new_stop=stops+1
                if new_stop==k+1 and nxt!=dst:
                    continue
                if new_cost<min_cost[nxt]:
                    min_cost[nxt]=new_cost
                    queue.append([new_stop,nxt,new_cost])
        return -1 if min_cost[dst] ==float('inf') else min_cost[dst]

