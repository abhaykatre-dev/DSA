class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # n=len(s)
        # mid=n//2

        # if n%2==0:
        #     left="".join(sorted(s[:mid]))
        #     return left+left[::-1]
        # else:
        #     left="".join(sorted(s[:mid]))
        #     return left+s[mid]+left[::-1]

        freq=[0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1

        left=[]
        mid=""
        for i in range(26):
            ch=chr(i+ord('a'))
            left.append(ch*(freq[i]//2))
            if freq[i]%2==1:
                mid=ch
        left="".join(left)
        return left+mid+left[::-1]
            

        
        
            