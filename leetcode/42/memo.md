# Step 1

11\. Container With Most Water が思い起こされ、two pointers でなんとかできないかしばらく考えていた（尺取りか、左右から狭めていくか）が、特に良さそうな方法が思いつかない。

少し発想を変えて、元々水が `max(height)`まで満たし、マップが水没していたとしたらどうか考えてみる。水は一番高い点から両方に向かって流れ出すから...一番高いところで分けて左右で反対の向きに処理していったらどうだろう。

水が隙間を埋めているから、左から見ていったら高さは単調増加していって、頂点から右は高さが単調現象していく。

キタ！ `step1.py` で解けた！ 30 分とかのコーディング面接中に自力で思いつけて回答を書き切れる自信はないが、自力で Hard 問題が解けて嬉しい。

two pointers は単調増加・減少を利用することが多いな、というか思いつく問題は全てそうだな。じゃないとpointer(s) を一方向に動かすだけでは問題が解けないもんな。

# Step 2

LeetCode の Solutions を眺めてみる。

[https://leetcode.com/problems/trapping-rain-water/solutions/5126477/video-keep-max-height-on-the-both-side-b-hv39/](https://leetcode.com/problems/trapping-rain-water/solutions/5126477/video-keep-max-height-on-the-both-side-b-hv39/)

```py
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water
```

狐につままれたような感覚だが、低い方の高さに cap されるからできるのだろう。11\. Container With Most Water みたいなやり方だなぁ。

自分でやり方を思いつけた嬉しさからかもしれないが、自分のやり方の方がアイデアが明確で伝えやすいと思った。何回か書いてみたら意見が変わるかもしれないが。
