# Step 1

まず、わざわざルートをとってユークリッド距離それ自体を計算する必要がなく、距離を二乗した値を比較しても大小関係が崩れない、というところが最初のキモのように感じた。

2通り思いつき、回答を書くのに特に引っかかりは覚えなかった。

## ヒープ

[LeetCode 703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)や[LeetCode 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)を思い出すと、kth (+それ以上・以下) の値を求めると聞くとHeapが一番最初に想起される。

各部分木において根が最大値になるmax heapを用いて、k個の点を保持 \& 現状k番目に大きい数と、新たに加える数を比較していけばいい。
Pythonのheapqはmin heapだが、入力する値に`-1`をかければmax heapになる。

時間計算量: O(nlogk)
空間計算量: O(k)

## ソート

単純に全ての距離 (の二乗) を計算、その値を用いてソートし、小さい順にk個取ってくればいい。

時間計算量: O(nlogn)
空間計算量: O(n), Timsort

# Step 2

LeetCode勉強会のDiscordには、PRが見当たらなかった。LeetCodeのSolutionsを眺めてみる。

## max heapの解法 (`step1_heap.py`) の改善案

Step 1では

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

とする解法もあった。どちらにせよ必要な処理を条件分岐から出すことで、若干私の脳への収まりがよくなったが、どちらの方が人気だろう。

## min heap -> `step2_min_heap.py`

max heapにk個の点だけ入れる方法と異なり、まず全ての点の (距離, 座標) を入れたリストをヒープ化し、そこからk個取り出す解法。

時間計算量: O(n + klogn), [heapq.heapify(x): Transform list x into a heap, in-place, in linear time.](https://docs.python.org/3/library/heapq.html#heapq.heapify)
空間計算量: O(n)

## quickselect -> `step2_quickselect.py`

LeetCodeのSolutionsを眺めていたら、SortやHeapを用いる方法以外に、Quickselectを用いる方法が目についた。確かに、Quickselect内のpartitioningにより、k番目の数が見つかった時点でそれより左にある数がk番目の数よりも小さくなっている。

時間計算量: 平均O(n), 最悪O(n^2)
空間計算量: O(n)

## その他悩んだこと

距離の二乗を保持する変数の名前をどうするか悩んだ。`distance`としてしまうと、厳密には違うような気がするのだが、修飾語をつけるとかなり冗長になってしまい逆に読みづらくなってしまうような気がする。コメントなどで補足するのがいいだろうか...。

