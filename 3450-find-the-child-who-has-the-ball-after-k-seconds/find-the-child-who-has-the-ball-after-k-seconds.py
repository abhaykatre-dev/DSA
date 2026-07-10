class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        pos=0
        direction=1
        for _ in range(k):
            if pos==0:
                direction=1
            if pos==n-1:
                direction=-1
            pos+=direction
        return pos