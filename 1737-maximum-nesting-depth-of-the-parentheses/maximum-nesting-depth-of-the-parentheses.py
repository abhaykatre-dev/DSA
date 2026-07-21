class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        stack=[]
        for ch in s:
            if ch=="(":
                stack.append(ch)
            elif ch==")":
                stack.pop()
            depth=max(depth,len(stack))
        return depth