import heapq


class MedianFinder:
    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.smaller, num)

        largest_in_smaller = heapq.heappop_max(self.smaller)
        heapq.heappush(self.larger, largest_in_smaller)

        while len(self.smaller) < len(self.larger):
            smallest_in_larger = heapq.heappop(self.larger)
            heapq.heappush_max(self.smaller, smallest_in_larger)

    def findMedian(self) -> float:
        if len(self.larger) < len(self.smaller):
            return float(self.smaller[0])

        return (self.smaller[0] + self.larger[0]) / 2
