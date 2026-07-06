# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack=[]
        arr=[]
        temp=head
        n=0
        while temp:
            n+=1
            arr.append(temp.val)
            temp=temp.next
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(arr[i])
        return ans