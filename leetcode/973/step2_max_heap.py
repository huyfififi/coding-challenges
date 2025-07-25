import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            distance = pow(x, 2) + pow(y, 2)
            heapq.heappush(heap, (-distance, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for _, point in heap]
