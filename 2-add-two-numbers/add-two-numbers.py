# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        temp=l1
        while temp:
            s1=str(temp.val)+s1
            temp=temp.next
        temp=l2
        while temp:
            s2=str(temp.val)+s2
            temp=temp.next
        s=str(int(s1)+int(s2))[::-1]
        dummy=ListNode(0)
        curr=dummy
        for ch in s:
            curr.next=ListNode(int(ch))

            curr=curr.next
        return dummy.next
        

        