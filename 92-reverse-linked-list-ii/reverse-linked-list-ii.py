# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp=head
        result=[]
        while temp:
            result.append(temp.val)
            temp=temp.next
        left-=1
        right-=1
        while left<right:
            result[left],result[right]=result[right],result[left]
            left+=1
            right-=1
        temp=head
        count=0
        while temp:
            temp.val=result[count]
            count+=1
            temp=temp.next
        return head
