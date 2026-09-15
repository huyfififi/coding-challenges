CHUNK_SIZE = 4


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        traversed: list[TreeNode | None] = []
        nodes = [root]
        while nodes and any(node for node in nodes if node is not None):
            next_nodes = []

            for node in nodes:
                traversed.append(node)
                if node is None:
                    next_nodes.append(None)
                    next_nodes.append(None)
                    continue

                next_nodes.append(node.left)
                next_nodes.append(node.right)

            nodes = next_nodes

        serialized: list[str] = []
        for node in traversed:
            if node is None:
                serialized.append("9999")
            else:
                serialized.append(str(node.val + 1000).rjust(4, "0"))

        return "".join(serialized)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None

        num_nodes = len(data) // CHUNK_SIZE
        chunks = []
        for i in range(num_nodes):
            chunk_data = data[CHUNK_SIZE * i : CHUNK_SIZE * (i + 1)]
            if chunk_data == "9999":
                chunks.append(None)
            else:
                chunks.append(int(chunk_data) - 1000)

        max_depth = 0
        while num_nodes > 0:
            max_depth += 1
            num_nodes = num_nodes // 2

        def build_tree(depth: int) -> list[TreeNode]:
            if depth == max_depth:
                return [None] * (2**depth)

            child_nodes: list[TreeNode] = build_tree(depth + 1)
            nodes = []
            for order_i, chunk_i in enumerate(
                range(2**depth - 1, 2 ** (depth + 1) - 1)
            ):
                if chunks[chunk_i] is None:
                    nodes.append(None)
                    continue

                node = TreeNode(chunks[chunk_i])
                node.left = child_nodes[2 * order_i]
                node.right = child_nodes[2 * order_i + 1]
                nodes.append(node)

            return nodes

        return build_tree(0)[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
