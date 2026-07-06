# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        n=1
        tail=head
        while tail.next:
            n+=1
            tail=tail.next
        k=k%n
        if k==0:
            return head
        tail.next=head #circular LL 
        curr=head
        for _ in range(n-k-1):
            curr=curr.next
        new_head=curr.next
        curr.next=None
        return new_head
        