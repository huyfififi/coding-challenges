import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, key=lambda p: pow(p[0], 2) + pow(p[1], 2))
