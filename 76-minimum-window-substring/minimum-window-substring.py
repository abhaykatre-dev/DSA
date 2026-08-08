class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        for ch in t:
            need[ch]=need.get(ch,0)+1
        window={}
        left=0
        have=0
        required=len(t)
        min_len=float('inf')
        min_start=0
        
        for right in range(len(s)):
            ch=s[right]
            if ch in window:
                window[ch]+=1
            else:
                window[ch]=1
            if ch in need and window[ch]<=need[ch]:
                have+=1
            while have==required:
                if right-left+1<min_len:
                    min_len=right-left+1
                    min_start=left
                left_ch=s[left]
                window[left_ch]-=1
                if left_ch in need and window[left_ch]<need[left_ch]:
                    have-=1
                left+=1
        if min_len==float('inf'):
            return ""
        return s[min_start:min_len+min_start]
                
