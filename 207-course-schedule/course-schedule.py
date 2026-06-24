from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist=[[] for _ in range(numCourses)]
        inDegree=[0]*numCourses
        for u,v in prerequisites:
            adjlist[u].append(v)
            inDegree[v]+=1
        queue=deque()
        result=[]
        for i in range(numCourses):
            if inDegree[i]==0:
                queue.append(i)
        while queue:
            curr_node=queue.popleft()
            for adjnode in adjlist[curr_node]:
                inDegree[adjnode]-=1
                if inDegree[adjnode]==0:
                    queue.append(adjnode)
            result.append(curr_node)
        
        if len(result)==numCourses:  
            return True
        else:
            return False


        
                    