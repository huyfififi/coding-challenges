# step 1

## Prefix Sum Array + Greedy

SubarrayのsumといえばPrefix Sum Array。一度Prefix Sum Arrayを作ったら、あとは[LeetCode 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)と同じ問題だな、と思った。

時間計算量: O(n)、空間計算量: O(n)

## 他の解法

Follow upでdivide and conquerが仄めかされていたので、どうにか問題を分割できないか考えていたのだが、思いつかなかった。
全体から見ると最大になるSubarrayも、部分問題で見たら最大になるとは限らないところに難しさがあるように思った。
