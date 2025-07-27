import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance_and_points = []
        for x, y in points:
            square_distance = x * x + y * y
            heapq.heappush(distance_and_points, (square_distance, [x, y]))

        answer = []
        for _ in range(k):
            _, point = heapq.heappop(distance_and_points)
            answer.append(point)
        return answer
