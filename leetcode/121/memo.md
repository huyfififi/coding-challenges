# Step 1

## 1. Brute-force Approach (Time Complexity: O(n^2), Space Complexity: O(1))

Check all pairs `(i, j)` where `i < j`, and calculate `prices[j] - prices[i]`. Track the maximum profit. Time complexity: O(n^2)

## 2A. Greedy Approach (Time Complexity: O(n), Space Complexity: O(1))

各ステップにおいて、暫定的な最大利益をトラックする。`i`日目の株価が過去最低値であった場合、それ以降の最大利益は（`i-1`日目までの最低値ではなく）`i`日目の株価を用いるので、variableに保持する。

逆に、最新の株価から見ていって過去最大の株価と比較していくやり方でもできる。

思いつきはするものの、うまく頭の中で整理・言語化できない。少し頭の中で寝かせておいた方がいいだろうか。

if文を排除して

```python
for i in range(1, len(prices)):
    min_price = min(prices[i], min_price)
    max_profit = max(prices[i] - min_price, max_profit)
```

としてしまえば行数が省けるのだが、`min()`が何をやっているのか読み解く負荷の方が今の私には大きく感じた。

また、

```python
import math
...
   min_price = math.inf
```

とすれば素直に`for price in prices`とできてシンプルに書けるのだが、余分なmoduleをimportしたくない気持ちと板挟みにあった。今回のケースでどちらが好まれるかは判断がつかなかった。`float("inf")`も、`int`と`float`のように型が違うものを保存・比較するのは落とし穴にハマりそうで忌避感があったが、これは後で調べてみようと思う。

## 2B. Recursive Approach (Time Complexity: O(n), Space complexity: O(n))

`i`日目までの最大利益は(`i-1`日目までの最大利益)又は(`i`日目の株価 - 過去最低額)

（結局はGreedyの解法とやっていることは変わらないのだろうが）こちらの方法の方が納得感がある。

# Step 2

## 参考にした他の方々のPR

- [seal-azarashiさんのPR](https://github.com/seal-azarashi/leetcode/pull/35)
	- 入力の`prices`がemptyである場合や`null`である場合も対処して`return 0`されていた。LeetCode上はさておき、私が業務でこういう関数を作るなら`assert prices`で想定外の入力を落とすかなぁ、と思ったが、さらに`prices`の中身まで確かめようとすると大変だとも思い、どこまで入力を信用すれば良いのか難しく感じた。
- [Ryotaro25さんのPR](https://github.com/Ryotaro25/leetcode_first60/pull/41)
	- seal-azarashiさんと同じく、最終的に`min_price = min(prices[i], min_price)`, `max_profit = max(prices[i], max_profit)`というif conditionを`min()`, `max()`に内包した形に落ち着いていて、こちらの方がわかりやすく感じる人が多そうに感じた。
- [TORUS0818さんのPR](https://github.com/TORUS0818/leetcode/pull/39)
	- liquo-riceさんが、`min_price`を更新したら（結果的には無視されるにせよ）その値を用いて`max_profit`を計算するのは同日の利益を計算していることになるので、`max_profit = max()`を先に計算すべきと指摘されていた。確かに、言われてみれば納得。
		- `min()`や`max()`がif 文を吸収してしまっていることにわかりにくさがあるように感じた。
- [olsen-blueさんのPR](https://github.com/olsen-blue/Arai60/pull/37)
- [hroc135さんのPR](https://github.com/hroc135/leetcode/pull/35)

## float("inf"), math.inf

```
In [1]: import math

In [2]: math.inf == float("inf")
Out[2]: True

In [3]: type(math.inf)
Out[3]: float
```

- [StackOverflow - What is the point of float('inf') in Python?](https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python)
- [Reddit - float('inf') is bad practice](https://www.reddit.com/r/Python/comments/1c4x7b7/floatinf_is_bad_practice/?rdt=41431)

匿名・意見が偏っている可能性が否めないが、ざっと眺める限り使用自体に忌避感を示す人は少なそう

`sys.maxsize`もあるようだが、Pythonのintが保持できる数の上限はないから

```python
In [1]: import sys

In [2]: sys.maxsize
Out[2]: 9223372036854775807

In [3]: n = sys.maxsize + 1

In [3]: n
Out[3]: 9223372036854775808

In [4]: n > sys.maxsize
Out[4]: True
```

とあり、infinityとして扱うのは不適かと思われる。

# Step 3

Step 2 と解法が変わらなかったので省略
