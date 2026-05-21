class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        

    def get(self, index: int) -> int:
        curr=self.head
        count=0
        while curr and count<index:
            curr=curr.next
            count+=1
        if curr:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        
    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
            return
        curr=self.head
        prev=None
        count=0
        while curr and count<index:
            prev=curr
            curr=curr.next
            count+=1      
        if count!=index:
            return 
        new_node=Node(val)
        prev.next=new_node
        new_node.next=curr 

    def deleteAtIndex(self, index: int) -> None:
        if index==0 and self.head:
            self.head=self.head.next
            return
        curr=self.head
        prev=None
        count=0
        while curr and count<index:
            prev=curr
            curr=curr.next
            count+=1
        if not curr:
            return
        prev.next=curr.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)