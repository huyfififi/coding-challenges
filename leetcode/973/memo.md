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

## heapq.nsmallest() -> `step2_heapq_nsmallest.py`

そういえば、この前[703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)をレビューさせていただいたとき、`nlargest()`を用いた解法に出会ったのを思い出した。さすがに面接では、`heapq.nsmallest()`や`heapq.nlargest()`のロジックを実装してほしいという話になるだろうが、一応頭の片隅に入れるために使用してみてメモしておく。

[Python Documentation - heapq.nsmallest](https://docs.python.org/3/library/heapq.html#heapq.nsmallest)

> Return a list with the n smallest elements from the dataset defined by iterable...Equivalent to: `sorted(iterable, key=key)[:n]`.

実装によっては最小のn個をとってくるだけでその順序は保証しないと (なぜか) 思い込んでいたが、結果のn個の値も昇順で並ぶのか。

[python/cpython/Lib/heapq.py](https://github.com/python/cpython/blob/a852c7bdd48979218a0c756ff1a5586d91cff607/Lib/heapq.py#L479)

以下 CPythonのリポジトリからコピペ。

```python
def heapreplace_max(heap, item):
    """Maxheap version of a heappop followed by a heappush."""

# ...

def heapify_max(x):
    """Transform list into a maxheap, in-place, in O(len(x)) time."""

# ...

def nsmallest(n, iterable, key=None):
    # ...omitted...

    # General case, slowest method
    it = iter(iterable)
    result = [(key(elem), i, elem) for i, elem in zip(range(n), it)]
    if not result:
        return result
    heapify_max(result)
    top = result[0][0]
    order = n
    _heapreplace = heapreplace_max
    for elem in it:
        k = key(elem)
        if k < top:
            _heapreplace(result, (k, order, elem))
            top, _order, _elem = result[0]
            order += 1
    result.sort()
    return [elem for (k, order, elem) in result]
```

最初にiterableの[:n]でmax heapを作って、iterableの[n:]の値を一つずつ比較・入れ替えしていき、最後に順序を保証するために`sort()`を呼んでいる。

なるほど、結局私 (やみなさんの) max heapを用いた解法とやっていることは変わらないな。

時間計算量: O(nlogk), 多めに見積もってn回のheap操作 O(logk) でO(nlogk)。最後にソートしている (O(klogk)) が、`k <= n`で、合わせてO(nlogk)。
空間計算量: O(k)

## その他悩んだこと

距離の二乗を保持する変数の名前をどうするか悩んだ。`distance`としてしまうと、厳密には違うような気がするのだが、修飾語をつけるとかなり冗長になってしまい逆に読みづらくなってしまうような気がする。コメントなどで補足するのがいいだろうか...。

heapの変数名にも悩んだ。heapであることを強調すべきか、heapなのは処理から明らかなので中身を表すべきか。
