# Step 1

## First Attempt

### Sort (Timsort)

Follow up もあるみたいだが、とりあえずベースの問題だけ解いてみる。
`list`をソートをしてしまえば、真ん中の値 (1つか2つ) にアクセスするだけで中央値が返せる。
Python の Timsort なら、ほぼほぼソートされた配列のソートは大体 `O(n)` で済むので、`addNum()` の呼び出しで毎回 `sort()` を呼んでも

> At most 5 * 10^4 calls will be made to addNum and findMedian.

という制約から、すごく大雑把に `5 * 10 ^ 4` 回 の 5 * 10 ^ 4 つの要素を走査する `addNum()` をすると `10 ^ 9` 回くらいの処理が必要になる。Python は大雑把に、1秒間に`10^6`回くらいの処理ができるので、トータルで大体 1000 秒くらいのオーダーかなと予想できる。これはLeetCodeでギリギリ通るくらいの処理時間だと記憶している。

シンプルな実装で通った -> `step1_sort.py`

といっても、これは Python のソートが Timsort であることを利用していて、C++ などでは同じ方法が取れないだろうと思うので、もう少し効率が良い方法があるだろう。少し考えてみる。

### Math-based

中央値の定義から数学的に？中央値を簡単に更新し続けられないかとも考えたが、 特に良さそうな方法は思いつかない。平均値なら簡単に値を再計算し続けられるような気がするが (total と size だけ記録すれば良い)、うまく言語化できないが、中央値ではうまくいかないように思う。

### balanced BST

各ノードが subtree の大きさを持つ Binary Search Tree を作ったらどうだろう。木が 歪んでいて一本の線のようになったら意味がないが、バランスが良い木を作れたら `addNum()` も `findMedian()` も O(log n) でできそう。基本的な BST の実装はできるが、re-balancing は今の私では実装できないので、一旦保留。

### Heap

Max Heap に 半分の要素数だけ、小さい方の数を入れていたらどうだろう？ -> 少し書いてみたが、たとえば [1, 2, 3, 4] の順で値が来た時に、まず [1, 2] を入れて、次に 3, 4 がきた時に値を捨ててしまい、5 が来た時に 5 を 小さい方に入れてしまうな、なんとか回避できないか -> 大きい方の数を入れる　Min Heap も用意すればできるのでは？ -> できた。`step1_heap.py`。面接中に書き上げられる自信はないが、今は自力でこの解法にたどり着けたことを嬉しく思う気持ちを尊重しよう。

他に良い方法も思いつかないので、一旦 follow up を 考えてみる。

## Follow Up

### If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

とりうる値の範囲が [0, 100] だとわかっているなら、その長さ分の配列を用意してカウントだけインクリメントさせていけばいいな。問題では言われていないが、0 と 100 を繰り返し hard code することに抵抗があったので、MIN, MAX を定義して、defaultdict を使った。

中央値は、単に真ん中の二つの値がどれかを走査して確認すればいい。

```py
import collections


class MedianFinder:
    MIN = 0
    MAX = 100

    def __init__(self):
        self.num_to_count = collections.defaultdict(int)
        self.size = 0

    def addNum(self, num: int) -> None:
        assert self.MIN <= num <= self.MAX
        self.num_to_count[num] += 1
        self.size += 1

    def findMedian(self) -> float:
        first_position = (self.size - 1) // 2
        second_position = self.size // 2

        count = 0
        first_num = None

        for num in range(self.MIN, self.MAX + 1):
            count += self.num_to_count[num]

            if first_num is None and first_position < count:
                first_num = num

            if second_position < count:
                return (first_num + num) / 2
```

UPDATE:

```py
self.counts = [0] * (self.MAX - self.MIN + 1)
```

の方が、direct addressing ができることを直接表現できたな。問題の制約的に、配列 + direct accessing が想定されているのだろう。

### If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

上の trick を使い回して、`<= -1` と `101 <=` の部分は別々にソートして持てば良いかなと思ったが、AIに聞いたところ、もっと効率的なやり方があるらしい。

> Yes — your idea works, but there’s an even stronger optimization hiding in this follow-up.

> If 99% of all values are in [0, 100], then the median must itself be somewhere in [0, 100]. The ≤1% outliers can’t occupy the middle of the sorted stream.

> So you actually *don’t need to keep the values outside [0,100] sorted at all*. You only need to know how many values are below 0 and how many are above 100.

確かに、99% が [0, 100] の範囲に収まるのならば、中央値もその中にあるから、上のコードに加えて、0 より小さい数と 100 より大きい数の個数だけ持って、その分中央値の計算をずらせばいいのか。なるほどね。

# Step 2

LeetCode の Solutions を眺めても、AIに聞いても、2 つの Heap を使う方法が想定解らしい。では、Step 1 の解法を綺麗にする。

[https://leetcode.com/problems/find-median-from-data-stream/solutions/74062/short-simple-javacpython-olog-n-o1-by-st-zu1r/](https://leetcode.com/problems/find-median-from-data-stream/solutions/74062/short-simple-javacpython-olog-n-o1-by-st-zu1r/)

この解法シンプルだ。私の Step 1 は必要以上に複雑だったな。[0] にアクセスしてしまうの、Python の heap が配列で実装されているのを知らない人には驚きを与えてしまうかなと思ったが、まぁPythonを書いている人ならわかるか。

defensive になるなら `while` が 2 ついるが... 今回の場合は一方向への変更のみの保証の方が読みやすい、ような気がする。

あ、あと Step 1 で 返り値を `float` にするのを忘れていた。問題はないだろうが、型ヒントに `-> float:` と書いてあるので `float()` するのが無難であろう。

`step2.py` ではまず larger に入れてから smaller に移し、smaller が larger よりも大きくなってしまうので、smaller と larger の大きさが同じか larger の方が smaller よりも 1 大きい状態にキープする方法。先に smaller に入れる方法と見比べてみたが... 今のところどちらが私の好みかは判別できない。どちらでも良いので、両方の書き換えができるようにした方がいいような気がする。

```py
import heapq


class MedianFinder:
    def __init__(self):
        self.negated_smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.negated_smaller, -num)

        largest_in_smaller = -heapq.heappop(self.negated_smaller)
        heapq.heappush(self.larger, largest_in_smaller)

        while len(self.negated_smaller) < len(self.larger):
            smallest_in_larger = heapq.heappop(self.larger)
            heapq.heappush(self.negated_smaller, -smallest_in_larger)

    def findMedian(self) -> float:
        if len(self.larger) < len(self.negated_smaller):
            return float(-self.negated_smaller[0])

        return (-self.negated_smaller[0] + self.larger[0]) / 2
```
