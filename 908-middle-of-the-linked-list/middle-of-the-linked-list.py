# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Tortoise-Hare Approach
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

        #brute-force
        # curr=head
        # length=0
        # while curr is not None:
        #     length+=1
        #     curr=curr.next
        # count=0
        # curr=head
        # while count<length//2:
        #     count+=1
        #     curr=curr.next
        # return curr
