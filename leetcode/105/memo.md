# Step 1

先日、レビュー依頼を受けて取り組んだのだが、初見ではいくら例をこねくり回してもさっぱりわからなかった (アルゴリズムに落とし込めなかった)。
前回取り組んだ際の私の理解では、

preorder では、左右の部分木より先に root が現れる。
inorder では、左・root・右 の順序が保たれる。

これを組み合わせて

preorder で見つけた root を inorder 内で探すと、その位置より左にある値は左の部分木、右にある値は右の部分木に属する。

これを再帰的に当てはめていけば、binary tree が一意に決まる。

TODO: 時間計算量・空間計算量

未だしっくりこないし、この理解が正しいか自信はないが、他の方々のPRを見てみることにする。

# Step 2

[mamo3grさんのPR](https://github.com/mamo3gr/arai60/pull/28/changes#diff-4298635e808820604d74d3c43a2bcce0a2e36a9627af25d32462a8c12e01beea)
- step 1 が私のものとほぼ同じに見えるが、インデックスを引き回さずコピーを渡すことで helper 関数を作らずに済んでいる。空間計算量は O(n^2) だが、今回の制約では大丈夫そうな範囲のように見受けられる。
- hash map の使用で、inorder内のrootの位置を探す操作を短縮する工夫。
- dataclass は個人的に普段あまり使用しないから思いつかなかった。ドキュメントを眺めてみよう。
	- [dataclasses - Data Classes - Python documentation](https://docs.python.org/3/library/dataclasses.html)
	- "This function is a decorator that is used to add generated special methods to classes, as described below..."
- Span を使用する解法を写経させていただいた。やっと preorder の区間を次にどう渡していくのか、わかりかけてきた気がする。`step2_span_based.py`
	- Time Complexity: O(n), Space Complexity: O(n) call stack in worst cases, hash map

[garunituleさんのPR](https://github.com/garunitule/coding_practice/pull/29)
- 写経 -> `step2_pick_preorder.py`
- Step 1 を考えていた時はうまく言語化できていなかったのだが、私の Step 1 の方法では、次の root をつけるために preorder を毎回スキャンする必要があった。
- この方法では、次に root になる preorder の位置を返して再帰間で共有できるため、余計な探索を省くことができていて、脳への収まりも良い。

# Step 3

お二方の方法を何回か自分の感覚で書き直していくうちにしっくりくるようになった。

## `step3_pick_next_root.py`

次に root として使うべき preorder の位置を渡していく。
