class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        coordinate_and_distances: list[tuple[list[int], int]] = []
        for x, y in points:
            coordinate_and_distances.append(([x, y], pow(x, 2) + pow(y, 2)))

        coordinate_and_distances.sort(key=lambda x: x[1])
        return [coord for coord, _ in coordinate_and_distances[:k]]
