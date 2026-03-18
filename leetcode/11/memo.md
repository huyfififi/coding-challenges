# Step 1

素直に全通り試すと 時間計算量は O(n^2)。

> 2 <= n <= 10^5

なので、C++ が 1秒間に10^9 回の処理が行えるとしても、大体 10 秒くらいのオーダーの処理時間がかかりそう。

しばらく考えてみたのだが、枝刈りは思いついても、時間計算量を O(nlogn) や O(n) にする方法が思いつかなかった。

# Step 2

LeetCode にポストされている Solution を見てみた。

```py
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

```

うーん？なんでTwo Pointersでうまくいくのだろう。少し考えてみる。

[thonda28 さんのPR](https://github.com/thonda28/leetcode/pull/16/changes#r1687386128)

[Segment Tree](https://en.wikipedia.org/wiki/Segment_tree) を用いた解法もあるようだ。実装できるまで理解するのにかなり時間がかかりそうだから一旦置いておこうか。
