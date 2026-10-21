# Step 1

一つの方法しか思いつかなかった。メモ化再帰をしていく方法で、全ての時間を舐めていって (`endTime[i] <= 10^9`)、一つの job を高々 1 回ずつしか処理しない (`1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4`) ので大体処理は `10 ^ 9 + 5 * 10 ^ 4` steps くらいで、処理時間的にはギリギリかなと思ったら Memory Limit Exceeded になった。-> `step1_memo_mle.py`

ヒントが、dp[i] -> i から始まる job を選んだ時の最大利得として dynamic programming をとのことだったが、よくわからなかった。

AI にLeetCode上のヒントを噛み砕いてもらっていたら解答が書けた -> `step1.py`
