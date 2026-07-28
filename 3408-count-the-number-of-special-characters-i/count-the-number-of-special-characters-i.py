class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        myset=set(word)
        cnt=0
        for ch in myset:
            # if ch.lower() in myset:
            #     cnt+=1
            
            if chr(ord(ch)+32) in myset:
                cnt+=1
        return cnt
            