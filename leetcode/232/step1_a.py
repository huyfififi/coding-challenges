class MyQueue:
    def __init__(self):
        self.start_stack = []
        self.end_stack = []

    def push(self, x: int) -> None:
        while self.end_stack:
            self.start_stack.append(self.end_stack.pop())
        self.start_stack.append(x)

    def pop(self) -> int:
        while self.start_stack:
            self.end_stack.append(self.start_stack.pop())
        return self.end_stack.pop()

    def peek(self) -> int:
        while self.start_stack:
            self.end_stack.append(self.start_stack.pop())
        return self.end_stack[-1]

    def empty(self) -> bool:
        return not self.start_stack and not self.end_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
