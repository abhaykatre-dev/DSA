# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        odd=head
        even=head.next
        even_head=even
        while even and even.next:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=even_head
        return head


        
        # if head is None or head.next is None:
        #     return head
        # temp=head
        # my_list=[]
        # while temp and temp.next:
        #     my_list.append(temp.val)
        #     temp=temp.next.next
        # if temp:
        #     my_list.append(temp.val)

        # temp=head.next
        # while temp and temp.next:
        #     my_list.append(temp.val)
        #     temp=temp.next.next

        # if temp:
        #     my_list.append(temp.val)
        # temp=head
        # count=0
        # while temp:
        #     temp.val=my_list[count]
        #     count+=1
        #     temp=temp.next
        # return head