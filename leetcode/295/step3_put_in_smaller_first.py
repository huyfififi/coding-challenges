import heapq


class MedianFinder:
    def __init__(self):
        self.negated_smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.negated_smaller, -num)

        largest_in_smaller = -heapq.heappop(self.negated_smaller)
        heapq.heappush(self.larger, largest_in_smaller)

        while len(self.negated_smaller) < len(self.larger):
            smallest_in_larger = heapq.heappop(self.larger)
            heapq.heappush(self.negated_smaller, -smallest_in_larger)

    def findMedian(self) -> float:
        if len(self.larger) < len(self.negated_smaller):
            return float(-self.negated_smaller[0])

        return (-self.negated_smaller[0] + self.larger[0]) / 2
