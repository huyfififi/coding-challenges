# Step 1

## Diameter of Binary Treeの理解

問題文を読んで、少し脳内でいくつか例を考えて見た結果、"diameter of binary tree"は`root`において (左の部分木の高さ) + (右の部分木の高さ)ではないかと考えた。しかし、いざ走らせてみると、パスしないテストケースが見つかった。
テストケースを見てよく考えてみると、diameterとなるpathはrootを経由しない場合もあり得るな、と気づいた。

## max depth vs height

[LeetCode 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)が脳内にちらついていたので、`max_depth`という見方をしていたが、`height`の方が端的に木の高さを表せて良いな、と`step1_recursive.py`の後考えた。

```
height = max depth (depth of the deepest node(s))
```

## Iterativeな解法

post-order traversalなので行きと帰りで別の操作を行う必要があり、pre-order traversalで解ける、例えば[LeetCode 226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)のようには素直なiterative解法が書けない。

# Step 2

## 先駆者の方々のPR

- [Jikuharaさん](https://github.com/Jikuhara/LeetCode/pull/5)
	- Helper関数の命名について、"また、計算はしているとは言えないため、 calculate で始めるのは違和感があります。"、確かに。
- [NobukiFukuiさん](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/36)
	- `calculate_diameter_and_depth`という命名
- [Kitaken0107さん](https://github.com/Kitaken0107/GrindEasy/pull/17)

## Type Hints

Type Hintsを律儀に書いてみたが、変数の中身が複雑なので、逆に読みづらくなってしまうような感覚を受けた。
LeetCodeが`Optional`を使用しているので、それに合わせているが、いつもなら`| None`と書いている。
また、[FastAPIのドキュメント](https://fastapi.tiangolo.com/it/python-types/#using-union-or-optional)で`Optional[A]`はわかりづらいから、`Union[A, None]`と書け、と目にしたことがある。が、Python 3.10以前についての記述であり、今では`A | None`が主流だろうか。

## Helper関数の命名

野田さんのご指摘の通り、計算しているわけではないので`calculate_*`は不適に思うが、良い代替案が思い浮かばない。

`get_*`はどうかな？と思ったが、The Art of Readable Codeに

> Many programmers are used to the convention that methods starting with `get` are *"lightweight accessors"* that simply return an internal member...

とされていて、時間計算量がO(1)かつ簡潔な処理で値が返る場合しか`get_*`を使いたくない気持ちがある。本の中では`compute_*`が代替案として例示されているが、これは結局`calculate`と変わらないだろう。
