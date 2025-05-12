# Step 1

典型的な動的計画法の問題。

あるstep(n)に1回の行動でたどり着くには、step(n - 1)から1回で1step登る場合とstep(n-2)から1回で2steps登る場合しかない。

n=0の入力は制約上あり得ないが、便宜上0stepの位置にいる場合の数は1通りだとして、再帰で書くと

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0, 1):
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```

時間計算量: O(2^n), 1つのfunction callから2つのfunction callsが生まれ、再起呼び出しが2分木のような構造になる。そして、その高さはn。
空間計算量: O(n), 最大でstackに積まれるfunction callはn

この方法だと

```
f(4)
= f(3) + f(2)
= 'f(2)' + f(1) + 'f(2)'
```

のように同じものを複数回計算してしまう。
素直に再帰関数で得られる部分問題の結果をhash mapに記録 (Memoization, top-down型のアプローチ) していけば同じ部分問題を複数回解かなくて済むのだが、
bottom-up型のアプローチとして、下からtable/arrayに結果を埋めていくTabulationがある。

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        num_ways = [None] * (n + 1)
        num_ways[0] = 1
        num_ways[1] = 1
        for i in range(2, n + 1):
            num_ways[i] = num_ways[i - 1] + num_ways[i - 2]
        return num_ways[n]
```

時間計算量: O(n)
空間計算量: O(n)

しかし今回の場合、あるステップの答えは、1つ前ののステップと2つ前のステップにのみ依存しているので、それら二つさえ保持していれば答えが出せて、空間計算量を O(1) にできる。

# Step 2

[NobukiFukuiさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/30)
[rihibさんのPR](https://github.com/rihib/leetcode/pull/35)
    - 結果をペアで返す方法については思い至らなかった。Balanced Binary Treeでも使用したテクニックだ。

こういう感じだろうか。

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def _climb_stairs_helper(m: int) -> tuple[int, int]:
            if m == 1:
                return 1, 1

            prev_1, prev_2 = _climb_stairs_helper(m - 1)
            return prev_1 + prev_2, prev_1

        return _climb_stairs_helper(n)[0]
```

`m`の値をprintしてみると線形時間で解けているよう。

```
m=10
m=9
m=8
m=7
m=6
m=5
m=4
m=3
m=2
m=1
```

例えを用いるなら、メモ化再帰は、部下全員が更新する共通のホワイトボードがあって、各人間が部下に(n-1)と(n-2)の仕事を託す際にホワイトボードのメモを見て、まだ埋まっていなかったら(複数の)部下に仕事を投げる方法。
対して、ペアを返す方法は、部下に自分の結果と、自分の部下の結果の二つを報告するようにお願いすれば、直接やりとりする部下が一人で済む。

# Step 3

色々な解法を試してみると、`1 <= n <= 45`なので空間計算量O(1)の解法とO(n)の解法のメモリ使用量にほとんど差が現れなかった。LeetCodeの実行結果は信頼度が高いものではないが。
