# Step 1

## BFS (`step1_bfs.py`)

最初は post-order traversal でなんとかできないかと思ったが、うまく問題設定に当てはまらない。
少し考えて、[LeetCode 102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/) をして、各深さに置いて最後のNodeの値だけ見ていけば良いのでは？と気づいた。
（直接上記のLeetCodeの問題を思い出したわけではなく、木といえばDFSかBFS、DFSはうまくいかなかったからBFSを検討したら、過去の実装が思い出された感じ。）

時間計算量 O(n), 空間計算量 O(n) (最悪の場合、Nodeが一列に並ぶ木において、答えのリストが長さnになる。また、完全二分木のように幅が大きい木の場合、BFSで保持するqueueのサイズが 最悪 O(n) になる)。


## DFS (`step1_dfs.py`)

少し考え直して、いつもなら left を right より先に処理するが、 right から処理すれば pre-order traversal でいけるのでは？と思った。

時間計算量 O(n), 空間計算量 O(n) (最悪の場合、Nodeが一列に並ぶ木において call stack と 答えを持つリストが n の長さを持つ)。
ただし、Node の数が高々100つなので、実行時間・メモリ使用量ともに問題ないだろう。

# Step 2

[cppreference.com - std::size\_t](https://en.cppreference.com/w/cpp/types/size_t.html)
勘違いをしていたのだが、`std::size_t`を使用するには `#include <cstddef>` をすべきなのか。primitive type だと思っていた。

LeetCode Solutions を眺めた感じ、自分の解法が一番わかりやすそうだったので、これで進むことにする。
