# Step 1

一旦 Follow Up は無視する。

Number of Island みたいにしたら解けるかなと思った。1 つ引っかかったのは、使用中のセルをどう除外するかで、典型的なBFS/DFSの問題のように global な `visited` フラグを持つのでは今回の問題設定の場合うまくいかないなと思った。少し考えてみると、使用中文字列を持てばよく、それも最近やった backtracking なら 1 つのフラグ配列を使いまわせる。
フラグ配列の代わりに、今まで通ったセルのリストを素直に持っても、高々 15 個の要素しか走査しなくて良いので、今回の制約的にそちらでもいい。

空間計算量 O(mn + L) (m = num of rows, n = num of cols, L = word length)
時間計算量 O(mn * 3 ^ L) (board全ての開始地点から、3分岐 (一つ前のマスには戻らない。最初だけ4分岐) を最大15回試すので)

制約が

> `1 <= m, n <= 6`
> `1 <= word.length <= 15`

なので、matrix の最大セル数 = used の最大サイズは 36。call stack は文字列の長さ分で 最大 15。メモリ使用量は問題ではなさそう。
実行時間は...少し混乱していたが、36 のスタート地点から、最大で 3 分岐 (一つ前のマスには戻らない。また、最初だけ4分岐) を 15 回 繰り返すので、大体 `36 * 4 * 3 ^ 14 ~= 7 * 10 ^ 8 (2の指数だったらある程度覚えているので暗算できるが、こういう計算はあまりパッとできないな)。Python が 1 秒間で大体 `10^6 - 10^7` 回の処理が行え、それが大体再帰・ループ処理と対応するとおくと、100 秒くらいかかるオーダーになってしまうだろうか。しかし、実際には早めにreturnしての枝刈りがかなり効いていそうだが...

## Follow Up

> **Follow up:** Could you use search pruning to make your solution faster with a larger board?

を考えてみる。枝刈り、という意味だよな？boardの大きさがとても大きいと考えると...

特に思いつかなかったので、LeetCode上のDiscussionを見てみると、

```py
        board_char_to_count = collections.Counter(itertools.chain.from_iterable(board))
        word_char_to_count = collections.Counter(word)
        for ch in word_char_to_count:
            if board_char_to_count[ch] < word_char_to_count[ch]:
                return False
```

というものが提示されていた。これを入れるだけでLeetCode上の実行時間ランキングでの順位が大きく上がった。

また、wordをひっくり返して word search を行っても同じ結果が得られるので、wordの先頭と末尾の文字のboard上での数を比べて、末尾の文字の個数の方が小さかったら word をひっくり返して search した方がDFSを始める回数が少なく済む。
この枝刈りもすると、LeetCode上での実行時間ランキングにおいてほぼトップになった。

なるほど、確かに言われてみれば納得感はあるが、面接中にスラスラと思いつけるかは自信がない。word をひっくり返して探索しても同じ、というのは問題文を読んでいて気づけた方がいいだろうな。

# Step 2

- [potrue さんのPR](https://github.com/potrue/leetcode/pull/74/changes)
	- 多少私と書き方が違うところ (使用済みセルの管理・returnの書き方) があるけれど、大枠として同じに見える。
