class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        neighbors = [set() for _ in range(n)]
        for node1, node2 in edges:
            neighbors[node1].add(node2)
            neighbors[node2].add(node1)

        remaining = n
        leaves = [node for node in range(n) if len(neighbors[node]) == 1]
        while remaining > 2:
            next_leaves = []
            for leaf in leaves:
                neighbor = neighbors[leaf].pop()  # only one should be left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    next_leaves.append(neighbor)
                remaining -= 1

            leaves = next_leaves

        return leaves
