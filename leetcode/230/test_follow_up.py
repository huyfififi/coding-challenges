from __future__ import annotations

import importlib

# Add new implementation modules here as they're created (e.g. "step2_follow_up").
MODULE_NAMES = ["step1_follow_up", "step2_follow_up", "step3_follow_up"]


def inorder(node) -> list[int]:
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def actual_size(node) -> int:
    if node is None:
        return 0
    return 1 + actual_size(node.left) + actual_size(node.right)


def assert_sizes_consistent(node) -> None:
    if node is None:
        return
    assert node.size == actual_size(
        node
    ), f"val={node.val}: size={node.size}, actual={actual_size(node)}"
    assert_sizes_consistent(node.left)
    assert_sizes_consistent(node.right)


def run_tests(BST) -> None:
    # insert builds a correctly ordered, correctly sized tree
    bst = BST()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(v)
    assert inorder(bst.root) == [2, 3, 4, 5, 6, 7, 8]
    assert bst.root.size == 7
    assert_sizes_consistent(bst.root)

    # delete a leaf
    bst.delete(2)
    assert inorder(bst.root) == [3, 4, 5, 6, 7, 8]
    assert_sizes_consistent(bst.root)

    # delete a node with a single child
    bst.delete(3)  # node 3 has only a right child (4)
    assert inorder(bst.root) == [4, 5, 6, 7, 8]
    assert_sizes_consistent(bst.root)

    # delete a node with two children (triggers successor splice)
    bst.delete(7)  # node 7 has both 6 and 8 as children
    assert inorder(bst.root) == [4, 5, 6, 8]
    assert_sizes_consistent(bst.root)

    # delete the root itself, when it has two children
    bst.delete(5)
    assert inorder(bst.root) == [4, 6, 8]
    assert_sizes_consistent(bst.root)

    # deleting down to a single node, then to an empty tree
    single = BST()
    single.insert(1)
    single.delete(1)
    assert single.root is None

    # root with exactly one child gets promoted correctly
    one_child = BST()
    one_child.insert(5)
    one_child.insert(3)
    one_child.delete(5)
    assert one_child.root is not None
    assert one_child.root.val == 3
    assert one_child.root.size == 1

    # find_kth_smallest against a freshly built tree
    kth_bst = BST()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        kth_bst.insert(v)
    for k, expected in enumerate([2, 3, 4, 5, 6, 7, 8], start=1):
        assert kth_bst.find_kth_smallest(k) == expected, k

    # find_kth_smallest after deletions
    kth_bst.delete(2)
    kth_bst.delete(7)
    remaining = sorted([3, 4, 5, 6, 8])
    for k, expected in enumerate(remaining, start=1):
        assert kth_bst.find_kth_smallest(k) == expected, k

    # find_kth_smallest on a right-skewed tree (ascending inserts)
    right_skewed = BST()
    for v in [1, 2, 3, 4, 5]:
        right_skewed.insert(v)
    for k, expected in enumerate([1, 2, 3, 4, 5], start=1):
        assert right_skewed.find_kth_smallest(k) == expected, k

    # find_kth_smallest on a left-skewed tree (descending inserts)
    left_skewed = BST()
    for v in [5, 4, 3, 2, 1]:
        left_skewed.insert(v)
    for k, expected in enumerate([1, 2, 3, 4, 5], start=1):
        assert left_skewed.find_kth_smallest(k) == expected, k

    # find_kth_smallest boundaries (k=1 and k=n) on a larger tree
    kth_bst2 = BST()
    for v in [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8]:
        kth_bst2.insert(v)
    sorted_vals = sorted([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8])
    assert kth_bst2.find_kth_smallest(1) == sorted_vals[0]
    assert kth_bst2.find_kth_smallest(len(sorted_vals)) == sorted_vals[-1]
    for k, expected in enumerate(sorted_vals, start=1):
        assert kth_bst2.find_kth_smallest(k) == expected, k


if __name__ == "__main__":
    for module_name in MODULE_NAMES:
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            print(f"Skipping {module_name} (not created yet)")
            continue

        run_tests(module.BST)
        print(f"All tests passed for {module_name}.")
