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

とすれば素直に`for price in prices`とできてシンプルに書けるのだが、余分なmoduleをimportしたくない気持ちと板挟みにあった。今回のケースでどちらが好まれるかは判断がつかなかった。`float("inf")`も、`int`と`float`のように型が違うものを比較するのは落とし穴にハマりそうで忌避感があったが、これは後で調べてみようと思う。

## 2B. Recursive Approach (Time Complexity: O(n), Space complexity: O(n))

`i`日目までの最大利益は(`i-1`日目までの最大利益)又は(`i`日目の株価 - 過去最低額)

（結局はGreedyの解法とやっていることは変わらないのだろうが）こちらの方法の方が納得感がある。
