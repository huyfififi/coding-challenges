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

わかった。
`i`, `j` (`i < j`, `height[i] < height[j]`) の2点を考える。面積は、高さが `height[i]` で決まるので、`(j - i) * height[i]`。
ここで、`j` をどれだけ減らしても、この面積を超えることはない。幅は小さくなる一方だし、`height[j]` が大きくなっても高さは `height[i]` で頭打ちだし、`height[j]` が小さくなれば高さも小さくなる。
だから `height[i] < height[j]` のときは、`j` を減らして得られる面積は最初のものを超えないので、試す必要がない。
`height[i] > height[j]` のときも同様。
なので、Two Pointersで解ける。

[thonda28 さんのPR](https://github.com/thonda28/leetcode/pull/16/changes#r1687386128)

[Segment Tree](https://en.wikipedia.org/wiki/Segment_tree) を用いた解法もあるようだ。
LeetCode の Solutions も眺めてみると、幾つか [Segment Tree を用いた解法](https://leetcode.com/problems/container-with-most-water/solutions/2998428/c-min-and-max-segment-tree-on-log10000-b-yh5c)が提示されている。

Segment Tree は区間内の最大値を返すことができて、今回の問題の場合、区間を高さ、値を `height` のインデックスに設定する。
あるインデックス `i` に対して、その `height[i]` の値以上の高さを持つ一番右のインデックスが面積の最大を作るので、区間 `[height[i], 10^4]` という クエリの返すインデックスとの面積をチェックしていけばいい。ただしこれだけだと、右側が`height[i]`以上になるような場合しかチェックしていないので、[5,4,3,2,1] のような入力を扱うために、逆方向にも同様にクエリを行い、左側にある最も遠いインデックスも調べる必要がある。
時間計算量は O(n log 10 ^ 4) = O(n)

いくつか解法をみてみたが、今の私には荷が重そうなので、一旦スキップさせていただくことにする。