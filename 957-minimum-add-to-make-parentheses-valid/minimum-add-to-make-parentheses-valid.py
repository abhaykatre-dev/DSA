class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
       
        for ch in s:
            if not stack or ch==stack[-1]:
                stack.append(ch)
            elif stack[-1]=='(' and ch==')':
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)
            