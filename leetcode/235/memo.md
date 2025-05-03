# Step 1

## Step 1-1 最初に考えた方法

各ノードに対して、左の部分木と右の部分木を全部探索して、`p`・`q`との位置関係を把握し、`p`と`q`が両方とも左の部分木にあれば左の部分木の結果を、`p`と`q`が両方とも右の部分木にあれば右の部分木の結果を返す。あるノードから見て`p`と`q`が左右に分かれているとき、そのノードはLowest Common Ancestor。

lowest common ancestorの解釈を少し変えているのでやや邪道な感じがするが、`p`と`q`が左右に分かれているパターンを判定するために、`q`を含まない`p`をrootとした部分木においても、`p`がlowest common ancestorだとしておく（`q`が部分木のrootの場合も同様に）。

各部分問題における返り値

- 今いるノードが`p`と`q`のどちらか -> どちらかがもう片方の直接の祖先（としておく）なので今いるノードを返す。
- 今いるノードにおいて、`p`と`q`の位置が左右に分かれている。 -> 今いるノードがLowest Common Ancestor
	- Lowest Common Ancestorのひとつ上のノードでは、`p`と`q`はまだ左右どちらかの部分木に固まっている。
- 上の二つが満たされない場合、`p`と`q`が左右どちらかに集まっているので、その部分木の結果を返す。

ノードの数をn、木の高さをhとすると、全てのノードに訪れるので時間計算量はO(n), 空間計算量はO(h) (スタックに積まれる関数呼び出しの最大量は木の高さ分)。

Binary Search Treeがbalancedであれば、h ~= log(2)n。Binary Search Treeが一直線に並んでしまっていたら h = n。

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

木の高さをhとして、木の階層を一つずつ下がっていくので

Iterativeな解法: 時間計算量 O(h), 空間計算量 O(1)

Recursiveな解法: 時間計算量 O(h), 空間計算量 O(h) (再帰呼び出しごとに関数コールがスタックに積まれるため)

ノードの数nと木の高さhの関係はstep 1-1に記した通り。

Binary Search Treeであるという制約を利用することで、各ステップにおいて左右どちらかの部分木だけを考えればよく、balanced BSTにおいて、時間計算量を O(n) -> O(log(2)n)に減らすことができた。

### 実装する上で悩んだところ

- `p_q_low`よりもいい変数名はないか
- while文はどう書いたら一番わかりやすいか。`while not (p_q_min <= root.val <= p_q_max)`は試したが、`root.val in (p_q_min, p_q_max)`と`p_q_min < root.val < p_q_max`という別の条件を合わせていて理解しづらい、かといって別々に書き下すとやや冗長に感じる。
- 問題文に"p and q will exist in the BST."とあるので、それらの祖先であるrootも正しく与えられるだろうと仮定した。

# Step 2

- [rihibさんのPR](https://github.com/rihib/leetcode/pull/29)
	- 私のstep1の解法のようにわざわざ`max(p.val, q.val)`をとらずに書き下してもわかりやすいなと感じた。
		- [先に大小関係を見ておくと冗長度が減らせる](https://github.com/rihib/leetcode/pull/29/files#r1742231005)という意見もある :eyes:
	- Go言語でどのようにエラーハンドリングするか考察されていた。
	- 私の`step1_2_recursive.py`では、明示的に`root`が`p`か`q`と重なった場合に対処していたが、これは`low <= root.val <= high`という条件に内包されているので、なくてもよかったなと気付かされた。
		- 私の頭の中の感覚だとあるnodeに対して`p`と`q`が左右に分かれている画と、nodeが`p`か`q`と重なっている画は別物なので分けて考えたい気持ちもあるが、少し時間を寝かせてみる。
- [thonda28さんのPR](https://github.com/thonda28/leetcode/pull/12)
	- ここでも、先に大小関係を見ておいてもいいんじゃないかという指摘。
- [Kitaken0107さんのPR](https://github.com/Kitaken0107/GrindEasy/pull/13)
	- 私は主語を1つ目のoperandにしたい気持ちがあるが、他の方々がどう思うかはまだ感覚がない。
- [colorboxさんのPR](https://github.com/colorbox/leetcode/pull/12)
	- pとqをswapさせてp.val < q.valを保証する方法は思いついていなかった。
- [NobukiFukuiさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/22)
	- 私は、iterativeで書いたとしても、部分問題を解いている感覚があるので`root`を別の変数におかず直接更新していく方が好みだが、少数派かもしれない。
	- シンプルな`small, large = min(p.val, q.val), max(p.val, q.val)`という命名

半日ほど時間をおいてみて、いざコードを書いてみると、先ほどは`root is p or root is q`と`min(p.val, q.val) < root.val < max(p.val, q.val)`は別のパターンであって同じ条件内に内包してしまうとわかりづらい、と主張したのだが、`p`・`q`が左右どちらかに寄っている場合は早めにループや関数から抜けていて、そこまでわかりづらくもないような気もしてきた。

# Step 3

Iterativeな解法もrecursionを使用した解法もほぼ同じになった。
