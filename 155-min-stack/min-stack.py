class MinStack:

    def __init__(self):
        self.items=[]
        self.minStack=[]
    def push(self, value: int) -> None:
        self.items.append(value)
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)

    def pop(self) -> None:
        if self.items.pop()==self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        
        return self.items[-1]

    def getMin(self) -> int:
        if not self.items:
            return None
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()