class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        mid=n//2

        if n%2==0:
            left="".join(sorted(s[:mid]))
            return left+left[::-1]
        else:
            left="".join(sorted(s[:mid]))
            return left+s[mid]+left[::-1]
            

        
        
            