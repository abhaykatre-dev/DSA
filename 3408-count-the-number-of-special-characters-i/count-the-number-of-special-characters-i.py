class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        cnt = 0
        for ch in s:
            if ch==ch.upper() and ch.lower() in s:
                cnt+=1
        return cnt