import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (pow(x, 2) + pow(y, 2), [x, y]))

        answer = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            answer.append(point)
        return answer
