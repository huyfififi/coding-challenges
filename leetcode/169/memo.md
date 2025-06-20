# Step 1

## Counter (`step1_counter.py`)

最初に素直に考えつく方法として、まず全ての要素の出現回数を数えて、次に半数を超える要素を見つけ次第returnする。
あとから考えると、全ての要素の個数を数えなくても、一回のループで個数のインクリメントと過半数チェックを行えば操作の回数を少なくできる。

時間計算量: O(n)
空間計算量: O(n)

## `n // 2 + 1` 番目に大きい数が答えであることを利用する方法

入力をソートした時、答えの数は過半数を占めているので、それが入力内で最小であったとしても、最大であったとしても、`n // 2 + 1`番目に大きい数 (`n // 2  if n is even else n // 2 + 1`番目に小さい数)が答えと一致する。

### Heap (`step1_heap_kth_largest.py`)

愚直に個数を数える方法の次に、[703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)の解法で`k = (n // 2) + 1`とすれば答えが求まるな、と思った。

時間計算量: O(nlogn), Heapの操作がO(logn)で、ループがO(n)
空間計算量: O(n), Heapの最大長が `n // 2 + 1`

### Sort (`step1_sort.py`)

Heapの解法を書いている途中に、ソートした方がはやくないか、と考えた。

時間計算量: O(nlogn), Pythonのソートアルゴリズムはinsertion sortとmerge sortを組み合わせたTimsortで、best case(入力が既にソートされている)の時の時間計算量はinsertion sortのO(n)。average/worst caseでmerge sortのO(nlogn)
空間計算量: O(n), best case時はinsertion sortのO(1)(?)、そうでない場合はmerge sortのO(n)。

### Quickselect (`step1_quick_select.py`)

[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

k番目に小さい数を見つけるなら、Quickselectもあるな、と記憶に残っていた。しかし、実際に調べながら実装して走らせてみると、Time Limit Exceededとなった。入力Arrayの数字が全て同じであった場合、範囲の分割が効率的に行われない（1つずつしか範囲が削られない）ため、時間計算量がO(n^2)かかってしまう。

時間計算量: O(n)。常に最小・最大の数を選んでしまったらO(n^2)、これは入力が全て同じ数である場合と、運悪くランダムに選んでくるpivotが全て最小または最大（現実的には確率は低い）場合に起きる。
空間計算量 (recursive): O(logn)。最悪の場合O(n)。

ざっとGoogle検索の結果を眺めてみたが、どのような書き方が一般的なのかわからなかった。

# Step 2

LeetCodeのSolutionsを覗いてみる。そういえば、Boyer–Moore majority vote algorithmというものがあったな。違う要素が出るたびに相殺し続けても、全体の過半数は最後まで"残りカウント"を失わない。

先駆者の方々のPRを見てみる。

- [kitakenさんのPR](https://github.com/Kitaken0107/GrindEasy/pull/19)
- [rihibさんのPR](https://github.com/rihib/leetcode/pull/37)

Discord上での、Boyer–Moore majority vote algorithmが常識的なものかどうかについての情報

- [https://discord.com/channels/1084280443945353267/1084283898617417748/1193461706857390100](https://discord.com/channels/1084280443945353267/1084283898617417748/1193461706857390100)
- [https://discord.com/channels/1084280443945353267/1084283898617417748/1194299632201777172](https://discord.com/channels/1084280443945353267/1084283898617417748/1194299632201777172)

常識には含まれないが、GoogleのSWEの中では知っている方が多いらしい :eyes:

# Feedback

There is no feedback on this pull request.
