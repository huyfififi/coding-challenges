class MedianFinder:
    def __init__(self):
        self.data: list[int] = []

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()

    def findMedian(self) -> float:
        if len(self.data) % 2 == 1:
            return self.data[len(self.data) // 2]
        else:
            return sum(self.data[len(self.data) // 2 - 1 : len(self.data) // 2 + 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
