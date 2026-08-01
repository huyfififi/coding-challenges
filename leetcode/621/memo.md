# Step 1

## ノーヒント

最初に考えたのは、全てのユニークなラベルを各ステップで一個ずつ消費していく方法だった。

```
[A, C, A, B, D, B], n = 1
step 1: remove [A, B, C, D]
step 2: remove [A, B]

4 + 2 = 6 intervals
```

しかし、これは

```
[A, B, C, D, A, A], n = 1
step 1: remove [A, B, C, D]
step 2: remove A + (idle)
step 3: remove A + (idle)

4 + 2 + 2 = 8 intervals
```

となり、

```
[A, B, A, C, A, D]

6 intervals
```

の順に処理すべき場合に上手くいかない。

この方法の上手くいっていないところは idle 部分を減らすために使用できるラベルを序盤で全て使用してしまうことにある。なので次に考えた方法は、一番出現頻度の高いタスクを先に間を挟んで並べておいて、そこに残りのタスクを並べていくものだった。

```
[A, B, C, D, A, A], n = 1

A, _, A, _, A, _
->
A, B, A, C, A, D
```

ただ、それだけだとユニークなタスクが埋めたいidleの数を超えて存在する場合（例えば `[A, A, A, B, B, B, C, C, C], n = 1`）どうすれば良いのかわからず詰まってしまった。

## ヒントを見たあと

Hint 2 まで見た。

> For every cycle, find the most frequent letter that can be placed in this cycle. After placing, decrease the frequency of that letter by one.

問題文を見た時は特に気にしていなかったのだが

> `tasks[i]` is an uppercase English letter.

という制約があるので、タスクの種類は最大 26種類。ということは、最頻のタスクをとってくることは `O(1)` で行える。-> 変数の書き間違いをして延々とハマってしまったが、最終的に解答を書き上げられた（`step1.py`）。

Hint 3 も見てみた。

> Use Priority Queue.

Hint 2 を見た時に、the most frequent latter をとってくるのは max heap できるなと思い、少しコードを書いていたのだが、上記の制約から priority queeu を使用しても大幅な処理時間の短縮にはつながらないだろうと考えて、単純なループを選択した。

少し考えてみたが、Heap の使用によりコードを大幅に改善する方法が思いつかなかったので、一旦他の方々の Solutions を見てみよう。
