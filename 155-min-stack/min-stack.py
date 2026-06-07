class MinStack:
    def __init__(self):
        self.items=[]
        self.minimum=float('inf')

    def push(self, value: int) -> None:
        self.minimum=min(self.minimum,value)
        self.items.append([value,self.minimum])

    def pop(self) -> None:
        if len(self.items)!=0:
            self.items.pop()
        if not self.items:  #when stack become empty reset minimum
            self.minimum=float('inf')
        else:
            self.minimum=self.items[-1][1]
        
    def top(self) -> int:
        if len(self.items)!=0:
            return self.items[-1][0]

    def getMin(self) -> int:    
        # return self.items[-1][1]
        return self.minimum
      


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()