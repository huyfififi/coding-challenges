# Step 1

BST でも一度 traverse しない限りはどちらの木にいくつ Node があるのかわからないと思った。なので、一度 traverse するのは仕方がないとして

- LeetCode で Kth といえば Heap -> `step1_heap.py`
	- Time Complexity: O(nlogk)
	- Space Complexity: O(h + k), call stack と heap
	- C/C++ はアセンブリとの距離が近く 1 秒間に大体 `10^8~9` 回の処理が行える。Pythonはそれより大体 100 倍くらい遅いので、`10^6` 回 / 秒くらい。`1 <= k <= n <= 10^4` なので、最悪 `10 ^ 4 * 4 log10 ~= 10 ^ 5` で 0.1 秒くらいの処理時間がかかると大まかに予想される。

- BST は Inorder で traverse すればソートされた値が得られる -> `step1_sorted_list.py`
	- Time Complexity: O(n)
	- Space Complexity: O(n)

意図的ではないが、1 週間ほど寝かせてみると、いやそもそも BST なのだから、今まで inorder で訪れた Node の数を数えていれば早めに探索を打ち切れるのではないか？

- Early-Terminating Inorder Traversal -> `step1_inorder_traversal_to_get_kth.py`
	- Time Complexity: O(h + k), まず一番左下まで行って、そこから k 個 Node を訪れる
	- Space Complexity: O(h)
	- AI にリファクタリングの案を相談してみたら、found フラグの代わりに Exception を使用する方法を提示してきた。あまり見ないような気がするが、面白いのでメモしておく。-> `step1_inorder_traversal_kth_exception.py`

> Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

とあるが、どう状況が変わるのかよくわからないので、AI にヒントを出してもらうことにする。

> Subtle hint: think about what happens at a single node during your inorder traversal. At the root, you don't know if the k-th smallest is in the left subtree, is the root itself, or is in the right subtree — that's exactly the "I can't tell how many nodes are on which side" problem you identified at the start. What's the one number, if stored at each node, that would let you answer that question locally, in O(1), without visiting either subtree?

Step 1 の解法をこれ以上速くするのは難しいのではないか、と混乱していたが、実際に Follow up で聞かれていたのは、問題設定が若干変わった際にどう対応したらいいか、ということだった。ここまでヒントを出されると、流石に各 Node に子の数を持てば、いちいち subtree を全部探索せずに済み、左右どちらに行くかだけ判断すればいいので O(h) で済む。また、insertion/deletion の際はそのNode の親の Node を root までたどりながら `size += 1` または `size -= 1` をすればいいので O(h)。

`size` を追加した場合の BST への挿入と削除を書こうとしたが、削除で詰まってしまった。一旦、この問題は follow up 以前のものとして扱って、時間がある時に 450\. Delete Node in a BST に取り組みたいと思う。

450\. Deelte Node in a BST に取り組んできた。

- pick largest in the left subtree -> `450_step1_predecessor.py`
- pick smallest in the right subtree -> `450_step1_successor.py`

Time Complexity は O(h)。一度目の predecessor (successor) の探索で h のノードを訪問。二度目の `deleteNode()` で`root.left` (`root.right`) から先ほどの predecessor (successor) まで行って (O(h)) そこで O(1) の繋ぎかえ。
