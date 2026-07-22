class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # for ch in letters:
        #     if ch>target:
        #         return ch
        # return letters[0]
        l,r=0,len(letters)-1
        while l<r:
            mid=(l+r)//2
            if letters[mid]>target:
                r=mid
            else:
                l=mid+1
        return letters[l] if letters[l]>target else letters[0]