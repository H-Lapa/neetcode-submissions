class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            minVal = min(self.minStack[-1], val)
        else:
            minVal = val
        self.minStack.append(minVal)
        

    def pop(self) -> None:
        if not self.stack:
            return 

        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return -1

        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minStack:
            return -1

        return self.minStack[-1]
        
