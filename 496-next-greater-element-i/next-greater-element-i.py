class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums2)
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(nums2[i])
        
        for i in range(len(nums1)):
            index=0
            while nums1[i]!=nums2[index]:
                index+=1
            nums1[i]=ans[index]
        return nums1