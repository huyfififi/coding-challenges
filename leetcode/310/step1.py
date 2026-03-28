class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        adjacents = [set() for _ in range(n)]
        degrees = [0] * n
        for node1, node2 in edges:
            adjacents[node1].add(node2)
            adjacents[node2].add(node1)
            degrees[node1] += 1
            degrees[node2] += 1

        removed = set()
        while n - len(removed) > 2:
            leaves = [node for node in range(n) if degrees[node] == 1]
            for leaf in leaves:
                for adj in adjacents[leaf]:
                    degrees[adj] -= 1
                    adjacents[adj].remove(leaf)

                degrees[leaf] -= 1
                adjacents[leaf].pop()
                removed.add(leaf)

        return [node for node in range(n) if node not in removed]
