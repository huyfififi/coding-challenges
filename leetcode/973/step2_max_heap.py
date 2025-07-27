import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance_and_points = []
        for x, y in points:
            square_distance = pow(x, 2) + pow(y, 2)
            heapq.heappush(distance_and_points, (-square_distance, [x, y]))
            if len(distance_and_points) > k:
                heapq.heappop(distance_and_points)
        return [point for _, point in distance_and_points]
