import functools


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        neighbors = [[] for _ in range(n)]
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        @functools.cache
        def get_height(node: int, parent: int) -> int:
            child_heights = (
                get_height(neighbor, node)
                for neighbor in neighbors[node]
                if neighbor != parent
            )
            return 1 + max(child_heights, default=0)

        node = 0
        height = get_height(0, -1)
        while True:
            for neighbor in neighbors[node]:
                neighbor_height = get_height(neighbor, -1)
                if neighbor_height < height:
                    node = neighbor
                    height = neighbor_height
                    break
            else:
                break

        for neighbor in neighbors[node]:
            if get_height(neighbor, -1) == height:
                return [neighbor, node]

        return [node]
