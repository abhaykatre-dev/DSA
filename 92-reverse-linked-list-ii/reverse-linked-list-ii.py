# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummynode=ListNode(0)
        dummynode.next=head
        leftprev=dummynode
        curr=head
        for _ in range(left-1):
            leftprev=curr
            curr=curr.next
        prev=None
        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        leftprev.next.next=curr
        leftprev.next=prev
        return dummynode.next
        

        # temp=head
        # result=[]
        # while temp:
        #     result.append(temp.val)
        #     temp=temp.next
        # left-=1
        # right-=1
        # while left<right:
        #     result[left],result[right]=result[right],result[left]
        #     left+=1
        #     right-=1
        # temp=head
        # count=0
        # while temp:
        #     temp.val=result[count]
        #     count+=1
        #     temp=temp.next
        # return head
