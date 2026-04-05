class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        neighbors = [[] for _ in range(n)]
        degrees = [0] * n

        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)
            degrees[node1] += 1
            degrees[node2] += 1

        leaves = [node for node in range(n) if degrees[node] == 1]
        remaining = n
        while remaining > 2:
            next_leaves = []
            for leaf in leaves:
                degrees[leaf] = 0
                remaining -= 1

                # Only one neighbor is active at this point since `leaf` is a leaf
                for neighbor in neighbors[leaf]:
                    if degrees[neighbor] == 0:
                        continue

                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        next_leaves.append(neighbor)

            leaves = next_leaves

        return leaves
