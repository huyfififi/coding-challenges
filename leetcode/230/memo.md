# Step 1

BST でも一度 traverse しない限りはどちらの木にいくつ Node があるのかわからないと思った。なので、一度 traverse するのは仕方がないとして

- LeetCode で Kth といえば Heap -> `step1_heap.py`
	- Time Complexity: O(nlogk)
	- Space Complexity: O(h + k), call stack と heap

- BST は Inorder で traverse すればソートされた値が得られる -> `step1_sorted_list.py`
	- Time Complexity: O(n)
	- Space Complexity: O(n)

意図的ではないが、1 週間ほど寝かせてみると、いやそもそも BST なのだから、今まで inorder で訪れた Node の数を数えていれば早めに探索を打ち切れるのではないか？

- Early-Terminating Inorder Traversal -> `step1_inorder_traversal_to_get_kth.py`
	- Time Complexity: O(h + k), まず一番左下まで行って、そこから k 個 Node を訪れる
	- Space Complexity: O(h)
	- AI にリファクタリングの案を相談してみたら、found フラグの代わりに Exception を使用する方法を提示してきた。あまり見ないような気がするが、面白いのでメモしておく。-> `step1_inorder_traversal_kth_exception.py`
