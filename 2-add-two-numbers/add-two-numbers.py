# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            total=x+y+carry
            carry=total//10
            curr.next=ListNode(total%10)
            curr=curr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next

        # s1=""
        # s2=""
        # temp=l1
        # while temp:
        #     s1=str(temp.val)+s1
        #     temp=temp.next
        # temp=l2
        # while temp:
        #     s2=str(temp.val)+s2
        #     temp=temp.next
        # s=str(int(s1)+int(s2))[::-1]
        # dummy=ListNode(0)
        # curr=dummy
        # for ch in s:
        #     curr.next=ListNode(int(ch))

        #     curr=curr.next
        # return dummy.next
        

        