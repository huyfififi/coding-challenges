# Step 1

典型的なbacktrackingの問題だろう。

> `1 <= nums.length <= 10`

より、多くても `2 ^ 10 = 1024` 通りしか試さなくてよいので、Pythonが大体 1 秒間に `10 ^ 6` (`~ 10^7`) 回くらいの処理が行えることを考えると、実行時間が問題となることは稀だろう。
また、再帰のスタックも最大で10つしか積まれないので、メモリ使用も問題ないだろうと予想する。

自前で Stack を用意すると、各要素に分岐ごとの状態を保持 -> list のコピーが必要になりそうで、簡潔に `append()` と `pop()` のセットが書けないので、call stack を使用するのが一番シンプルだろう。

# Step 2

[mamo3grさんのPR](https://github.com/mamo3gr/arai60/pull/48/changes#diff-6a30cc55e4bab1e9213caa238344d14f218bd612284b839fe54cf6eea9765551)

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = [[]]
        for num in nums:
            all_subsets += [subset + [num] for subset in all_subsets]
        return all_subsets
```

なるほど、いくつか例を頭の中で確かめると動くことがわかるけど、一発では思いつかないな。勉強になる。

[itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product) を使用する方法も提示されている。

イメージとして、

(None, None), (None, num2)
(num1, None), (num1, num2)

を何重にもやるような感じだろうか。
