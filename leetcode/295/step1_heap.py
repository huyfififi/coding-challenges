import heapq


class MedianFinder:
    def __init__(self):
        self.negated_smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        if len(self.negated_smaller) == 0:
            heapq.heappush(self.negated_smaller, -num)
            return

        larger_in_smaller = -heapq.heappop(self.negated_smaller)
        heapq.heappush(self.negated_smaller, -larger_in_smaller)
        if num < larger_in_smaller:
            heapq.heappush(self.negated_smaller, -num)
        else:
            heapq.heappush(self.larger, num)

        while len(self.negated_smaller) <= len(self.larger):
            smallest_in_larger = heapq.heappop(self.larger)
            heapq.heappush(self.negated_smaller, -smallest_in_larger)

        while len(self.larger) + 1 < len(self.negated_smaller):
            largest_in_smaller = -heapq.heappop(self.negated_smaller)
            heapq.heappush(self.larger, largest_in_smaller)

    def findMedian(self) -> float:
        total_size = len(self.negated_smaller) + len(self.larger)
        if total_size % 2 == 1:
            median = -heapq.heappop(self.negated_smaller)
            heapq.heappush(self.negated_smaller, -median)
            return float(median)
        else:
            largest_in_smaller = -heapq.heappop(self.negated_smaller)
            heapq.heappush(self.negated_smaller, -largest_in_smaller)

            smallest_in_larger = heapq.heappop(self.larger)
            heapq.heappush(self.larger, smallest_in_larger)
            return (largest_in_smaller + smallest_in_larger) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
