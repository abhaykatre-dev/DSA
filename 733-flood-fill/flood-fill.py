class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        row=len(image)
        col=len(image[0])
        visited=deepcopy(image)
        intialcolor=image[sr][sc]
        def func(i,j):
            if i<0 or i==row or j<0 or j==col:
                return
            if visited[i][j]!=intialcolor:
                return
            if visited[i][j]==color:
                return
            visited[i][j]=color
            func(i+1,j)
            func(i-1,j)
            func(i,j+1)
            func(i,j-1)
        func(sr,sc)
        return visited