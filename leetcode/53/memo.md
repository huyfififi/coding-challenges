# Step 1

## Prefix Sum Array + Greedy

SubarrayのsumといえばPrefix Sum Array。一度Prefix Sum Arrayを作ったら、あとは[LeetCode 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)と同じ問題だな、と思った。

時間計算量: O(n)、空間計算量: O(n)

## 他の解法

Follow upでdivide and conquerが仄めかされていたので、どうにか問題を分割できないか考えていたのだが、思いつかなかった。
全体から見ると最大になるSubarrayも、部分問題で見たら最大になるとは限らないところに難しさがあるように思った。

# Step 2

## 他の方々のPR

### [potrueさんのPR](https://github.com/potrue/leetcode/pull/32)

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
