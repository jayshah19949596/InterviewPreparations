class MyQueue:

    def __init__(self):
        self.stack = []
        self.aux_stack = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.stack: self.front = x
        while self.stack:
            self.aux_stack.append(self.stack.pop())
        self.aux_stack.append(x)
        while self.aux_stack:
            self.stack.append(self.aux_stack.pop())

    def pop(self) -> int:
        popped_element = self.stack.pop()
        if self.stack:
            self.front = self.stack[-1]
        else:
            self.front = None
        return popped_element

    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        if len(self.stack) > 0:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()