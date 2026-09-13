# Step 1

一旦、返り値が `str` ではなくてもいいなら、と考える。
`rtype: list[int]`で実装できれば、制約より`-1000 <= Node.val <= 1000`なので、強引に各ノードを4桁の数字で表現して `str` を返すのはできそうかも。

例えば存在しない子も勘案する形で preorder traversal した場合の結果を返すのはどうだろう。

```
  1
 / \
2   3
   / \
  4   5
```

は `[1,2,null,null,3,4,null,null,5,null,null]`

これだけを見て元に戻せればいいのだが... 特に思いつかない。

次に思いついたのは、全てのノードが二つの子を持つ（とみなす, perfect binary tree）のはどうだろう、というアイデアだ。例えば上記の例では

```
1 段目 [1]
2 段目 [2, 3]
3 段目 [null, null, 4, 5]
```

とすれば、それが [1, 2, 3, null, null, 4, 5] だったとしも、最初の要素 (`2^0`) が1段目、次の `2^1` が 2段目、... となり、復元できそう (具体的な実装方法は頭の中で明瞭ではないが / 私の能力的にアイデアとコードにまだ距離がある)。

serialize は BFS したあと `9999 -> null`、 `0 ~ 2000 -> x - 1000` とすればstr変換もできそう。

~serialize で訪れるノードは制約より最大で `10^4`. deserialize は最後の段に追加で持つのも含めて `10^5`。~と思ったのだが、間違いに気づく。

`step1_mle.py` を書き、提出すると 51/53 のテストケースで Memory Limit Exceeded した。AI にヒントを出してもらいつつ考えると、私の方法では入力の木を全てのノードが2つの子を持ち葉が同じ深さになるように変更を加えているのだが、入力がバランスの悪い木であった場合に、変更に大量の操作が必要になってしまう。例えば、一直線の木を考えると、制約から最大深さは`10^4 - 1`、そして上記の操作を行なって木にpaddingを行うと、ノードの数が`2 ^ (10 ^ 4) - 1` になってしまう。

また、他に時間を溶かしたバグとして、私の方法では全てのノードが4桁の数字で表されるべきなのに、パディングを忘れてしまい桁が足りなくなってしまったのがあった。

## AI に教えてもらう

> The standard approach is preorder DFS with explicit null markers, using a delimiter so tokens can be variable-length (no fixed-width padding needed): ...

とのことだったので、DFS で書いてみる。-> `step1.py`

preorder, delimiter を使えば良いのだとわかったら思った以上にすんなり書けた。

AI に iterator を使う方法と deque を使う方法もあるよと言われたのでやってみる。

- `step1_iter_next.py`
- `step1_deque_popleft.py`

変数名にしっくりくるものが思いつかなかったが、Step 2 でもう少し考えてみたり他の方々のコードを確認したりすることにする。

## inorder & postorder

inorder と postorder で同じ方法ができるのか考えてみたのだが、inorderだとこのままの方法ではserialized されたものが区別できない木の形があるから不可能だろう。

```
1
 \
  3
 /
2
```

と

```
1
 \
  2
   \
    3
```

は inorder だと同じ 1 -> 2 -> 3 の順で訪れ、同様の方法で serialize すると `#,1,#,2,#,3,#` になるから 一意に deserialize できない。

postorder は preorder と順番が反対になるだけなので、deque で左側から pop する代わりに list (かそのままdeque) で右側から pop すればできそう。-> `step1_postorder.py`

# Step 2

## LeetCode Solutions を眺めてみる

DFS (Preorder) で解くコードは私が Step 1 で実装したものとほとんど変わらないが、

[https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/6932485/bfs-most-easy-implementation-java-c-java-xaqh](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/6932485/bfs-most-easy-implementation-java-c-java-xaqh)

は BFS で行えている。`deserialize()` がすんなりと理解できないが、とりあえず写経してみる。TODO: `step2_bfs.py`

## 変数名

`serialized` という変数名の代わりを考えていたのだが、`tokens` や `values` しか思いつかない。ある程度短くて意味がある程度通じるものとしては妥協で `serialized` でいいかなと思う。
