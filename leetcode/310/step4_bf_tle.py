from collections.abc import Iterator


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        neighbors = [[] for _ in range(n)]
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        def get_height(node: int, parent: int) -> int:
            child_heights: Iterator[int] = (
                get_height(neighbor, node)
                for neighbor in neighbors[node]
                if neighbor != parent
            )
            return 1 + max(child_heights, default=0)

        min_height = float("inf")
        min_height_roots = []
        for node in range(n):
            height = get_height(node, -1)

            if height < min_height:
                min_height = height
                min_height_roots = [node]
            elif height > min_height:
                continue
            else:
                min_height_roots.append(node)

        return min_height_roots
