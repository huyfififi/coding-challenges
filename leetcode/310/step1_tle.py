class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        node_to_adjacents = collections.defaultdict(list)
        for node1, node2 in edges:
            node_to_adjacents[node1].append(node2)
            node_to_adjacents[node2].append(node1)

        def traverse(node: int, visited: list[bool]) -> int:
            if visited[node]:
                return 0

            visited[node] = True
            child_height = 0
            for adj in node_to_adjacents[node]:
                child_height = max(child_height, traverse(adj, visited))
            visited[node] = False
            return 1 + child_height

        visited = [False] * n
        root_to_height = {}
        for root in range(n):
            root_to_height[root] = traverse(root, visited)

        min_height = min(root_to_height.values())
        mht_roots: list[int] = []
        for root, height in root_to_height.items():
            if height == min_height:
                mht_roots.append(root)
        return mht_roots
