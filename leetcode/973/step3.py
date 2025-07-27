import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            square_distance = x * x + y * y
            heapq.heappush(heap, (-square_distance, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for _, point in heap]
