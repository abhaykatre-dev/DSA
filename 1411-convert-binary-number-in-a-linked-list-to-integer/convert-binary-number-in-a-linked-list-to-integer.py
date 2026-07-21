# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        pow=0
        ans=0
        for i in range(len(arr)-1,-1,-1):
            ans+=(2**pow)*arr[i]
            pow+=1
        return ans