# Step 1

まず、わざわざルートをとってユークリッド距離それ自体を計算する必要がなく、距離を二乗した値を比較しても大小関係が崩れない、というところが最初のキモのように感じた。

2通り思いつき、回答を書くのに特に引っかかりは覚えなかった。

## ヒープ

[LeetCode 703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)や[LeetCode 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)を思い出すと、kth (+それ以上・以下) の値を求めると聞くとHeapが一番最初に想起される。

各部分木において根が最大値になるmax heapを用いて、k個の点を保持 \& 現状k番目に大きい数と、新たに加える数を比較していけばいい。
Pythonのheapqはmin heapだが、入力する値に`-1`をかければmax heapになる。

## ソート

単純に全ての距離 (の二乗) を計算、その値を用いてソートし、小さい順にk個取ってくればいい。

TODO: 時間・空間計算量

# Step 2

LeetCode勉強会のDiscordには、PRが見当たらなかった。LeetCodeのSolutionsを眺めてみる。

Sortする方法・Heapを用いる方法以外に、Quickselectをする方法もあった。最悪O(n^2)かかるのでTLEするだろうが、確かにk番目に小さい値を見つけたら、Quickselectのpartition操作により、arr[:k]を返せば答えになりそう。-> `step2_quickselect_tle.py` (TODO)

Heapの解法についてだが、Step 1では

```
if len(heap) < k:
    heapq.heappush(dist_and_point)
else:
    heapq.heappushpop(dist_and_point)
```

としたが、どちらにせよheapにpushしているので

```
heapq.heappush(heap, dist_and_point)
if len(heap) > k:
    heapq.heappop()
```

とする解法もあった。どちらにせよしなければならない処理を条件分岐から出すことで、若干私の脳への収まりがよくなったが、どちらの方が人気だろう。

また、max heapではなくmin heapを使う方法もあって、確かに、そういう方法もあるな、と新鮮さを感じた。一応こちらもやってみる。

距離の二乗を保持する変数の名前をどうするか悩んだ。`distance`としてしまうと、厳密には違うような気がするのだが、修飾語をつけるとかなり冗長になってしまい逆に読みづらくなってしまうような気がする。コメントなどで補足するのがいいだろうか...。

## min heap

max heapにk個の点だけ入れる方法と異なり、まず全ての点の (距離, 座標) を入れたリストをヒープ化し、そこからk個取り出す解法。

時間計算量: O(n + klogn), [heapq.heapify(x): Transform list x into a heap, in-place, in linear time.](https://docs.python.org/3/library/heapq.html#heapq.heapify)
空間計算量: O(n)
