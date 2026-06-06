# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        left=head
        right=prev

        while left and right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True

        #brute-force
        # temp=head
        # myList=[] 
        # while temp:
        #     myList.append(temp.val)
        #     temp=temp.next
        # st=0
        # end=len(myList)-1    
        # while st<end:
        #     if myList[st]!=myList[end]:
        #         return False
        #     st+=1
        #     end-=1
        # return True