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
    TreeNode* lowestCommonAncestor(
        TreeNode* root, TreeNode* p, TreeNode* q
    ) {
        if (root == p) { return p; }
        if (root == q) { return q; }
        bool is_p_on_left = Contains(root->left, p);
        bool is_q_on_left = Contains(root->left, q);
        if (is_p_on_left && is_q_on_left) {
            return lowestCommonAncestor(root->left, p, q);
        }
        if (!is_p_on_left && !is_q_on_left) {
            return lowestCommonAncestor(root->right, p, q);
        }
        return root;
    }
private:
    bool Contains(const TreeNode* root, const TreeNode* target) {
        if (root == nullptr) { return false; }
        if (root == target) { return true; }
        return Contains(root->left, target) || Contains(root->right, target);
    }
};
