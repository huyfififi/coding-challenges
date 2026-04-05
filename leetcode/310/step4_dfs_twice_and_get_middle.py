"""
First attempt using two DFS passes to find the longest path (diameter) and return its middle node(s).
I haven't carefully reviewed or refactored yet.
TODO:
- Revisit review comments
- Improve/refactor this solution.
"""


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        neighbors = [[] for _ in range(n)]
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        def find_farthest(
            node: int, visited: list[bool]
        ) -> tuple[int, int]:  # (farthest node, path length)
            path_length = 1
            farthest = node
            visited[node] = True
            for neighbor in neighbors[node]:
                if visited[neighbor]:
                    continue

                farthest_from_neighbor, path_length_from_neighbor = find_farthest(
                    neighbor, visited
                )

                if path_length_from_neighbor + 1 > path_length:
                    path_length = path_length_from_neighbor + 1
                    farthest = farthest_from_neighbor

            visited[node] = False
            return farthest, path_length

        longest_path_start, _ = find_farthest(0, [False] * n)
        longest_path_end, longest_path_length = find_farthest(
            longest_path_start, [False] * n
        )

        longest_path = []

        def traverse(node: int, end: int, visited: list[bool], path: list[int]) -> None:
            nonlocal longest_path

            path.append(node)
            if node == end:
                longest_path = path.copy()
                path.pop()
                return

            visited[node] = True

            for neighbor in neighbors[node]:
                if visited[neighbor]:
                    continue
                traverse(neighbor, end, visited, path)

            path.pop()
            visited[node] = False

        traverse(longest_path_start, longest_path_end, [False] * n, [])

        if longest_path_length % 2 == 1:
            return [longest_path[longest_path_length // 2]]
        else:
            return longest_path[
                longest_path_length // 2 - 1 : longest_path_length // 2 + 1
            ]
