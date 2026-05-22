# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       
        #Floyd’s Cycle Detection or Tortoise and Hare Algorithm TC=O(n),SC=(1)
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

        # #brute-force TC,SC=O(n)
        # my_set=set()
        # temp=head
        # while temp:
        #     if temp in my_set:
        #         return True
        #     my_set.add(temp)
        #     temp=temp.next
        # return False


