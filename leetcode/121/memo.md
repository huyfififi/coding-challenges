# Step 1

## 1. Brute-force Approach (Time Complexity: O(n^2), Space Complexity: O(1))

Check all pairs `(i, j)` where `i < j`, and calculate `prices[j] - prices[i]`. Track the maximum profit. Time complexity: O(n^2)

## 2A. Greedy Approach (Time Complexity: O(n), Space Complexity: O(1))

`i`日目の株価が過去最低値であれば、これから先の未来で`i-1`日目までの最低値が`i+1`日目以降の最大値との組み合わせにより最大利益をもたらすことはないので、`i`日目の株価を保持しておく。

思いつきはするものの、うまく頭の中で整理・言語化できない。少し頭の中で寝かせておいた方がいいだろうか。

## 2B. Recursive Approach (Time Complexity: O(n), Space complexity: O(n))

`i`日目までの最大利益は(`i-1`日目までの最大利益)又は(`i`日目の株価 - 過去最低額)

こちらの方法の方が納得感がある。
