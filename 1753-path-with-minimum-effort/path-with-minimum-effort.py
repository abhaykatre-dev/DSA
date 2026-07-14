import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        effort_arr=[[float('inf') for _ in range(cols)] for _ in range(rows)]
        effort_arr[0][0]=0
        priority_queue=[[0,0,0]]
        while priority_queue:
            eff,i,j=heapq.heappop(priority_queue)
            if i==rows-1 and j==cols-1:
                return eff
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                dx,dy=i+x,j+y
                if dx<0 or dy<0 or dx==rows or dy==cols:
                    continue
                new_eff=max(eff,abs(heights[dx][dy]-heights[i][j]))
                if new_eff<effort_arr[dx][dy]:
                    effort_arr[dx][dy]=new_eff
                    heapq.heappush(priority_queue,[new_eff,dx,dy])