import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance_and_point_heap: list[tuple[int, list[int]]] = []
        for x, y in points:
            square_distance = pow(x, 2) + pow(y, 2)
            if len(distance_and_point_heap) < k:
                heapq.heappush(
                    distance_and_point_heap,
                    (-square_distance, [x, y]),
                )
            else:
                heapq.heappushpop(distance_and_point_heap, (-square_distance, [x, y]))

        return [point for _, point in distance_and_point_heap]
