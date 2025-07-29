class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance_and_points = []
        for x, y in points:
            distance_and_points.append((pow(x, 2) + pow(y, 2), [x, y]))
        distance_and_points.sort()
        return [point for _, point in distance_and_points[:k]]
