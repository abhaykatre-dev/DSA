# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                ans=self.get_cycle_start(head,fast)
                return self.get_cycle_start(head,fast)
        return None

    def get_cycle_start(self,head,fast):
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
        #brute force
        # my_set=set()
        # temp=head
        # while temp:
        #     if temp in my_set:
        #         return temp
        #     my_set.add(temp)
        #     temp=temp.next
        # return None
