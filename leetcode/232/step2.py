class MyQueue:
    def __init__(self):
        self.front_elements = []  # front of queue is at end of list
        self.rear_elements = []  # rear of queue is at end of list

    def push(self, x: int) -> None:
        self.rear_elements.append(x)

    def pop(self) -> int:
        if not self.front_elements:
            while self.rear_elements:
                self.front_elements.append(self.rear_elements.pop())
        return self.front_elements.pop()

    def peek(self) -> int:
        if not self.front_elements:
            while self.rear_elements:
                self.front_elements.append(self.rear_elements.pop())
        return self.front_elements[-1]

    def empty(self) -> bool:
        return not self.front_elements and not self.rear_elements


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
