# Step 1

Cracking The Coding Interviewで取り組んだ記憶がある。

Binary Search Treeならもっと簡単な方法があるように思ったが、そのような制約はなさそうなので、root, p, q の位置関係で確認していくしかないかなと思った。親へのリンクもない。

lowestではないancestorだったらpとqの両方が左右どちらかの部分木にいる。pとqが左右に散ったところがlowest common ancestor。

# Step 2

Cracking the Coding Interviewを見てみた。親へのリンクがない場合の解法が私のStep 1と同じだった。ただ、これを最適化して各Nodeを一回ずつのみ探索する方法があるらしい。

以下、Cracking The Coding Interviewに載っている解法をC++で書き起こしたもの。

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        auto [common_ancestor, is_ancestor] = LowestCommonAncestorHelper(root, p, q);
        return common_ancestor;
    }
private:
    // is_ancestor == true -> node is the lowest common ancestor
    // is_ancestor == false -> node is either p or q
    struct NodeAndIsAncestor {
        TreeNode* node;
        bool is_ancestor;
    };
    // Returns
    // - a pointer to either p, q, or their lowest comon ancestor if exists
    // - a flag indicating whether the returned node is confirmed as a lowest common ancestor
    NodeAndIsAncestor LowestCommonAncestorHelper(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) { return NodeAndIsAncestor(root, false); }
        if (root == p && root == q) { return NodeAndIsAncestor(root, true); }

        NodeAndIsAncestor left_result = LowestCommonAncestorHelper(root->left, p, q);
        if (left_result.is_ancestor) { return left_result; }

        NodeAndIsAncestor right_result = LowestCommonAncestorHelper(root->right, p, q);
        if (right_result.is_ancestor) { return right_result; }

        if (left_result.node != nullptr && right_result.node != nullptr) {
            return NodeAndIsAncestor(root, true);
        } else if (root == p || root == q){
            bool is_ancestor = left_result.node != nullptr || right_result.node != nullptr;
            return NodeAndIsAncestor(root, is_ancestor);
        } else {
            if (left_result.node != nullptr) {
                return NodeAndIsAncestor(left_result.node, false);
            } else {
                return NodeAndIsAncestor(right_result.node, false);
            }
        }
    }
};
```

フラグによってhelper関数の返すノードの意味が変化すること、また条件分岐を読み解くのに時間がかかることから、個人的には非常に読みづらい気がしたので、現実的にはあまり真似できる解法ではないかなと思った。

追記: PRを作ってから読み返してみたら、これはフラグの使用により、すぐ下の解法から曖昧さを排したバージョンの解法なのか。合点いった (気がする)。TODO: またあとで眺めてみる。

LeetCodeのSolutionsを眺めたら、以下のような解法がポストされていた。

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) { return nullptr; }
        if (root == p || root == q) { return root; }

        TreeNode* left_lca = lowestCommonAncestor(root->left, p, q);
        TreeNode* right_lca = lowestCommonAncestor(root->right, p, q);

        if (left_lca != nullptr && right_lca != nullptr) {
            return root;
        }

        if (left_lca != nullptr) {
            return left_lca;
        } else {
            return right_lca;
        }
    }
};
```

シンプルだ。便宜上、pしかいない部分木のLCAはpである (部分木にpまたはqしかいなければそれを返し、両方存在すればLCAを返す) と置くことで、処理を簡潔にできている。pとqが与えられているTree内に必ず存在するという制約を利用している。
この、厳密には違うのだが、便宜上捉え方を変えることにより処理をシンプルにする、ということを以前やったことがある気がする。
自分のLeetCode練習メモを遡ったら、235. Lowest Common Ancestor of a Binary Search Tree にあった。[https://github.com/huyfififi/coding-challenges/pull/10/changes#diff-a85bba0a3335858bea809ef42cf2918e9208e78ca28f844af1e68ae5b48c295dR7](https://github.com/huyfififi/coding-challenges/pull/10/changes#diff-a85bba0a3335858bea809ef42cf2918e9208e78ca28f844af1e68ae5b48c295dR7)

> lowest common ancestorの解釈を少し変えているのでやや邪道な感じがするが、`p`と`q`が左右に分かれているパターンを判定するために、`q`を含まない`p`をrootとした部分木においても、`p`がlowest common ancestorだとしておく（`q`が部分木のrootの場合も同様に）。

昔の自分だったら最初に思いついていた方法だったのか。235のstep1がまんま上の解法だな。

関数の返り値に複数の意味を持たせるのは混乱するから、どちらが読みやすいかと言えば私は`Contains()`を利用した今回のstep 1 の方が読みやすいと思う。pとqの存在が前提であることは変わらないのだが...。

# Step 3

部分木にpまたはqしか存在しないとき、それを返す方法のとき、`lowestCommonAncestor()`の返す値がうまく簡潔に表現できなかったので、`left`、`right`としておいた。
