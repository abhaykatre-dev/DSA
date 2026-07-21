class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        curr=0
        for ch in s:
            if ch=="(":
                curr+=1
            elif ch==")":
                curr-=1
            depth=max(depth,curr)
        return depth