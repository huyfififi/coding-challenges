# Step 1

典型的な動的計画法の問題。再帰で書くと

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0, 1):
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```

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

しかし今回の場合、あるステップの答えは、1つ前ののステップと2つ前のステップにのみ依存しているので、それら二つさえ保持していれば答えが出せて、空間計算量を O(1) にできる。
