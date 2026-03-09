# Step 1

最初は post-order traversal でなんとかできないかと思ったが、うまく問題設定に当てはまらない。
少し考えて、[LeetCode 102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/) をして、各深さに置いて最後のNodeの値だけ見ていけば良いのでは？と気づいた。
（直接上記のLeetCodeの問題を思い出したわけではなく、木といえばDFSかBFS、DFSはうまくいかなかったからBFSを検討したら、過去の実装が思い出された感じ。）
