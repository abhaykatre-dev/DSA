class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_mat=[[float('inf') for _ in range(n)] for _ in range(n)]
        for i,j,d in edges:
            adj_mat[i][j]=d
            adj_mat[j][i]=d
        for i in range(n):
            adj_mat[i][i]=0
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adj_mat[i][via]!=float('inf') and adj_mat[via][j]!=float('inf'):
                        adj_mat[i][j]=min(adj_mat[i][j],adj_mat[i][via]+adj_mat[via][j])
        
        min_neighbor=n
        city=-1
        for i in range(n):
            count=0
            for j in range(n):
                if adj_mat[i][j]<=distanceThreshold:
                    count+=1
            if count<=min_neighbor:
                min_neighbor=count
                city=i
        return city