class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        neighbors = [[] for _ in range(n)]
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        def get_longest_path(node: int, parent: int) -> list[int]:
            longest_child_path = []
            for neighbor in neighbors[node]:
                if neighbor == parent:
                    continue

                child_path = get_longest_path(neighbor, node)
                if len(child_path) > len(longest_child_path):
                    longest_child_path = child_path

            return [node, *longest_child_path]

        path_from_zero = get_longest_path(0, -1)
        diameter_start = path_from_zero[-1]

        diameter = get_longest_path(diameter_start, -1)
        if len(diameter) % 2 == 1:
            return [diameter[len(diameter) // 2]]
        else:
            return diameter[len(diameter) // 2 - 1 : len(diameter) // 2 + 1]
