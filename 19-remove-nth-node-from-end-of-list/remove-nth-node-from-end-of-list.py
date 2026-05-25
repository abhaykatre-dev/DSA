# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #one pass optimal solution
        slow,fast=head,head
        for _ in range(n):
            fast=fast.next
        if fast is None:
            return head.next # when n points to head so just remove head and move next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head 
        # temp=head
        # count=0
        # while temp:
        #     count+=1
        #     temp=temp.next
        # temp=head
        # prev=None
        # if count==n:
        #     head=head.next
        #     return head
        # temp=head
        # prev=None
        # for i in range(count):
        #     if i==count-n:
        #         prev.next=temp.next
        #         return head
        #     prev=temp
        #     temp=temp.next
        # return head
           
                


