# Step 1

まず、わざわざルートをとってユークリッド距離それ自体を計算する必要がなく、距離を二乗した値を比較しても大小関係が崩れない、というところが最初のキモのように感じた。

2通り思いつき、回答を書くのに特に引っかかりは覚えなかった。

## ヒープ

[LeetCode 703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)や[LeetCode 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)を思い出すと、kth (+それ以上・以下) の値を求めると聞くとHeapが一番最初に想起される。

各部分木において根が最大値になるmax heapを用いて、k個の点を保持 \& 現状k番目に大きい数と、新たに加える数を比較していけばいい。
Pythonのheapqはmin heapだが、入力する値に`-1`をかければmax heapになる。

## ソート

単純に全ての距離 (の二乗) を計算、その値を用いてソートし、小さい順にk個取ってくればいい。
