class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r=0,len(height)-1
        l_max=r_max=0
        water=0
        while l<r:
            l_max=max(height[l],l_max)
            r_max=max(height[r],r_max)
            if l_max<r_max:
                water+=l_max-height[l]
                l+=1
            else:
                water+=r_max-height[r]
                r-=1
        return water


        # n=len(height)
        # leftmax=[0]*n
        # leftmax[0]=height[0]
        # for i in range(1,n):
        #     leftmax[i]=max(leftmax[i-1],height[i])
        # rightmax=[0]*n
        # rightmax[n-1]=height[n-1]
        # for i in range(n-2,-1,-1):
        #     rightmax[i]=max(rightmax[i+1],height[i])
        
        # TP=0
        # for i in range(n):
        #     TP+=min(leftmax[i],rightmax[i])-height[i]
        # return TP
        
        