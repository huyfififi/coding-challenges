# Step 1

## Prefix Sum Array + Greedy

SubarrayのsumといえばPrefix Sum Array。一度Prefix Sum Arrayを作ったら、あとは[LeetCode 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)と同じ問題だな、と思った。

時間計算量: O(n)、空間計算量: O(n)

## 他の解法

Follow upでdivide and conquerが仄めかされていたので、どうにか問題を分割できないか考えていたのだが、思いつかなかった。
全体から見ると最大になるSubarrayも、部分問題で見たら最大になるとは限らないところに難しさがあるように思った。

# Step 2

## 他の方々のPR

- [potrueさんのPR](https://github.com/potrue/leetcode/pull/32)

私と同じ方針だが、prefix sum arrayを先に作らずに、ループ内で累積和を更新していけば、空間計算量 O(1) で済んでいる。

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cumulative_sum = 0
        min_cumulative_sum_so_far = 0
        max_subarray_sum = -float("inf")

        for num in nums:
            cumulative_sum += num
            max_subarray_sum = max(
                max_subarray_sum, cumulative_sum - min_cumulative_sum_so_far
            )
            min_cumulative_sum_so_far = min(cumulative_sum, min_cumulative_sum_so_far)

        return max_subarray_sum
```

- [SatorienさんのPR](https://github.com/Satorien/LeetCode/pull/32)

Divide and conquerの解法について言及されていた。しばらく眺めてもよくわからなかったので、他の方々のPRも先に見てみることにする。

- [ryooooooryさんのPR](https://github.com/ryoooooory/LeetCode/pull/35)

丁寧に (brute-force ->) DP -> 部分和 という思考ステップが記録されていた。累積和に飛びついた私よりも、こちらの思考ステップの方が納得感がある。

- [Kazuryu0907さんのPR](https://github.com/Kazuryu0907/LeetCode_Arai60/pull/5)

動的計画法。f(i)をiで終わるsubarrayの最大値だとすると、f(i) = max(f(i - 1) + nums[i], nums[i])。
なるほど、こういう見方をすれば再帰的な関係が置けて、動的計画法ができるのか。

空間計算量を削らず、Kazuryu0907さんの考え方を自分なりに解釈すると以下のようになるだろうか。

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # max_ending_subarray_sum[i] -> i で終わるsubarrayの最大値
        max_ending_subarray_sums: list[int] = [0] * (len(nums) + 1)
        max_ending_subarray_sums[0] = float("-inf")

        for i, num in enumerate(nums):
            max_ending_subarray_sums[i + 1] = max(
                max_ending_subarray_sums[i] + num, num
            )

        return max(max_ending_subarray_sums)
```

- [tokuhiratさんのPR](https://github.com/tokuhirat/LeetCode/pull/32)

私とほぼ同じstep 1の発想とstep 3にある最終的なコード。

## Kadane's Algorithm

tokuhiratさんのPRでも言及されていたが、別の問題のPRをレビューしている時に Kadane's Algorithmというものに遭遇した記憶があった。
上の動的計画法のコードから空間計算量を削ったコードで、あるインデックスで終わる部分和の最大値、というところが発想のキモであるように感じた。
長さ0のsubarrayを許容する問題設定の場合、部分和 or 今指している値、の後者を0にすればい良い。

一般常識には含まれないらしい。

```python
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_subarray_sum = -float("inf")
        max_ending_subarray_sum = 0
        for num in nums:
            max_ending_subarray_sum = max(max_ending_subarray_sum + num, num)
            max_subarray_sum = max(max_subarray_sum, max_ending_subarray_sum)
        return max_subarray_sum
```

## その他

### Divide and Conquer

LeetCodeのSolutionsをざっと眺めて、一晩寝てもよくわからなかった。LeetCodeのSolutions上に残してあるコメントや、一社内のPRを見て予想するに、多くの人は分割統治法を思いつけない・書けないし、現在の私の理解力を超えているように思うので、一旦スキップすることにする。後で戻ってきた時にわかるようになっているかも。

### 変数名

Kadane's Algorithmの解法の変数に対して、端的で明確な名付けができなかった。変数名がやけに長くなってもしょうがないし、ある程度短いものにして、あとは処理から推測してもらう方がいいだろうか。

# Step 3

初期値が`0`でも`float("-inf")`でもいい時(`max_ending_sum`)、どちらを採用しようか迷う。
また、先にDPの解法があってから空間計算量を削ってKadane's Algorithm、という流れを欠いて、Kadane's Algorithmだけを一発目で見ると理解に時間がかかるような気がする。
