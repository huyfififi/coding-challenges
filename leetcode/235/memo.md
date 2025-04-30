# Step 1

## Step 1-1 最初に考えた方法

各ノードに対して、左の部分木と右の部分木を全部探索して、`p`・`q`との位置関係を把握し、`p`と`q`が両方とも左の部分木にあれば左に、`p`と`q`が両方とも右の部分木にあれば右に。

終了条件

- 今いるノードが`p`と`q`のどちらか -> どちらかがどちらかの直接の祖先
- 今いるノードにおいて、`p`と`q`の位置が左右に分かれている。 -> 今いるノードがLowest Common Ancestor
	- Lowest Common Ancestorのひとつ上のノードでは、`p`と`q`はまだ左右どちらかの部分木に固まっている。

木が一直線に伸びている状況を考えると、各ノードで部分木を全探索してしまうと (n - 1) (深さ0のとき)  + (n - 2) (深さ1のとき) + (n - 3) + ... で時間計算量が O(n^2)になりそう。

## Step 1-2

よく考えたら、せっかくBinary Search Treeが与えられているのに、その性質を利用していなかった。`root`, `p`, と`q`の位置関係はvalueを見るだけでわかるから、それを使えば直感的に書けそう （アハ体験（死語？））。

> All Node.val are unique.

という制約も見逃していた。

- [CS 225| Binary Search Tree](https://courses.grainger.illinois.edu/cs225/fa2019/notes/bst/)
- [Are duplicate keys allowed in the definition of binary search trees?](https://stackoverflow.com/a/300968/16193058)

を見るとBinary Search Treeの定義の中に全ての値がuniqueであることが含まれているように読み取れるが、

- [Stanford CS Education Library - Binary Trees](http://cslibrary.stanford.edu/110/BinaryTrees.html)

では同じ値を許容するようにも読み取れる。

いずれにしても、今回の問題では上の制約により、値だけ確認すれば3つのNodeの位置関係がわかることには変わりないだろう。

### 計算量

グラフ内のノードの数をNとして

Iterativeな解法: 時間計算量 O(N), 空間計算量 O(1) (worst case)

Recursiveな解法: 時間計算量 O(N), 空間計算量 O(N) (worst case, 再帰呼び出しごとに関数コールがスタックに積まれるため)

木の高さ分しか操作が繰り返されないので、Binary Search Treeがbalancedだった場合は O(N)であるところが -> O(logN)。

### 実装する上で悩んだところ

- `p_q_low`よりもいい変数名はないか
- while文はどう書いたら一番わかりやすいか。`while not (p_q_min <= root.val <= p_q_max)`は試したが、`root.val in (p_q_min, p_q_max)`と`p_q_min < root.val < p_q_max`という別の条件を合わせていて理解しづらい、かといって別々に書き下すとやや冗長に感じる。
- 問題文に"p and q will exist in the BST."とあるので、rootもあるだろうと仮定した。
