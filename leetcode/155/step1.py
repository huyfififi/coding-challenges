class MinStack:
    def __init__(self):
        self.num_and_prefix_min = []

    def push(self, val: int) -> None:
        if not self.num_and_prefix_min:
            self.num_and_prefix_min.append((val, val))
        else:
            prev_prefix_min = self.getMin()
            self.num_and_prefix_min.append((val, min(val, prev_prefix_min)))

    def pop(self) -> None:
        self.num_and_prefix_min.pop()

    def top(self) -> int:
        return self.num_and_prefix_min[-1][0]

    def getMin(self) -> int:
        return self.num_and_prefix_min[-1][1]
