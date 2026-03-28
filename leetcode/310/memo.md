# Step 1

素直に全ての root を試す方法しか思いつかなかった -> `step1_tle.py`。

後から思ったが、cycle がないことが保証されているので、一つ前に戻るのだけスキップする形の方がシンプルだった。

```py
            for adj in node_to_adjacents[node]:
                if adj == parent:
                    continue
                child_height = max(child_height, 1 + height(adj, node))
            return child_height
```

制約が

> `1 <= n <= 2 * 10^4`

で、全ての n から探索を行うと `(2 * 10^4) * (2 * 10^4) = 4 * 10^8`。
C++ が 1 秒間に `10^8 ~ 10^9` ステップの処理を行えるとすると、Pythonがそれより大体 100 倍遅いから 1 秒間で `10^6 ~ 10^7` ステップ。
なので、大体 `10 ~ 100` 秒くらいの実行時間になりそう。これは LeetCode 上でギリギリ Time Limit Exceeded になるかならないかくらいなので、微妙。案の定、TLEになった。

そのまま実装するとTLEになりそうなのはわかっていたので、何かしらのヒューリスティックが思いつかないか、考えてみて、一つ思い浮かんだのは、枝が一番多いノードを root として選ぶと木の高さが最小になるのでは、と思ったが、幾つか例を試してみると、うまくいかないことがわかった。

```
    5
    |
0 - 1 - 2 - 3 - 4
    |
    6
```

上の例だと、2 が本当の最小の高さを作る root。

LeetCode 上の Hint を考えてみる。

> How many MHTs can a graph have at most?

幾つか例を考えてみると、雑に考えてグラフの端から端までいく最長のパスかあって、それの真ん中のノードが 1 つか 2 つあり、それが Minimum Height Tree を形成しそう？
結構時間を使ってしまったので、悔しいが、解法を見てしまうことにする。

Discord 上で取り組まれた方はいなさそうなので、LeetCode の Solutions を眺めてみると、これらの記事が理解しやすそう

[dietpepsi - Share some thoughts](https://leetcode.com/problems/minimum-height-trees/solutions/76055/share-some-thoughts-by-dietpepsi-mjsc/)
[lc\_1000xCoder - [ Full Explanation ] BFS - Remove Leaf Nodes](https://leetcode.com/problems/minimum-height-trees/solutions/5060930/full-explanation-bfs-remove-leaf-nodes-b-4x00/)

まず、Minimum Height Tree を作る root は 1 つか 2 つという私の考えは正しかった。それをどう求めるのかだが、各ステップで現在の葉ノードを全て削除していって、最後に残った 1 個か 2 個のノードがグラフの一番長いパスの真ん中 -> Minimum Height Tree の root(s) になる。

やり方だけ頭において、LeetCode 207\. Course Schedule のように書いたら、`step1.py` のようになった。
