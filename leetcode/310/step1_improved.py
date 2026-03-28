class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        adjacents = [set() for _ in range(n)]
        degrees = [0] * n
        for node1, node2 in edges:
            adjacents[node1].add(node2)
            adjacents[node2].add(node1)
            degrees[node1] += 1
            degrees[node2] += 1

        leaves = [node for node in range(n) if degrees[node] == 1]
        remaining = n
        while remaining > 2:
            next_leaves = []
            for leaf in leaves:
                for adj in adjacents[leaf]:
                    adjacents[adj].remove(leaf)
                    degrees[adj] -= 1
                    if degrees[adj] == 1:
                        next_leaves.append(adj)

                degrees[leaf] -= 1
                adjacents[leaf].pop()
                remaining -= 1

            leaves = next_leaves

        return leaves
