class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if k==len(cardPoints):
            return sum(cardPoints)

        leftSum,rightSum=0,0
        n=len(cardPoints)
        maxi=0
        for i in range(0,k):
            leftSum+=cardPoints[i]
        maxi=max(maxi,leftSum)
        rightIndex=n-1
        for i in range(k-1,-1,-1):   
            leftSum-=cardPoints[i]
            rightSum+=cardPoints[rightIndex]
            maxi=max(maxi,leftSum+rightSum)
            rightIndex-=1
        return maxi
            