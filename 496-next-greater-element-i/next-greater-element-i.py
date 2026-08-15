class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dict={}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                dict[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        ans=[]
        for num in nums1:
            if num in dict:
                ans.append(dict[num])
            else:
                ans.append(-1)
        return ans