import heapq


class MedianFinder:
    def __init__(self):
        self.negated_smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.larger, num)

        smallest_in_larger = heapq.heappop(self.larger)
        heapq.heappush(self.negated_smaller, -smallest_in_larger)

        while len(self.larger) < len(self.negated_smaller):
            largest_in_smaller = -heapq.heappop(self.negated_smaller)
            heapq.heappush(self.larger, largest_in_smaller)

    def findMedian(self) -> float:
        if len(self.negated_smaller) < len(self.larger):
            return float(self.larger[0])

        return (-self.negated_smaller[0] + self.larger[0]) / 2
