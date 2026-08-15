class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        freq={}
        left=0
        maxlen=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen


        # n=len(s)
        # maxi=0
        # for i in range(0,n):
        #     my_set=set()
        #     for j in range(i,n):
        #         if s[j] in my_set:
        #             break
        #         maxi=max(maxi,j-i+1)
        #         my_set.add(s[j])
        # return maxi