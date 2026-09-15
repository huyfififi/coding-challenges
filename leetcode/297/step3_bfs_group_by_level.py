import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    DELIMITER = ","
    NULL_NODE = "#"

    def serialize(self, root):
        nodes = collections.deque([root])
        tokens = []
        while nodes:
            next_nodes = []
            for node in nodes:
                if node is None:
                    tokens.append(self.NULL_NODE)
                    continue

                tokens.append(str(node.val))
                next_nodes.append(node.left)
                next_nodes.append(node.right)

            nodes = next_nodes

        return self.DELIMITER.join(tokens)

    def deserialize(self, data: str) -> TreeNode | None:
        tokens = iter(data.split(self.DELIMITER))
        root_token = next(tokens)
        if root_token == self.NULL_NODE:
            return None

        root = TreeNode(int(root_token))
        nodes = collections.deque([root])
        while nodes:
            next_nodes = []
            for node in nodes:
                left_token = next(tokens)
                if left_token != self.NULL_NODE:
                    node.left = TreeNode(int(left_token))
                    next_nodes.append(node.left)

                right_token = next(tokens)
                if right_token != self.NULL_NODE:
                    node.right = TreeNode(int(right_token))
                    next_nodes.append(node.right)

            nodes = next_nodes

        return root
