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

        bool is_p_on_left = Covers(root->left, p);
        bool is_q_on_left = Covers(root->left, q);
        if (is_p_on_left && is_q_on_left) {
            return lowestCommonAncestor(root->left, p, q);
        } else if (!is_p_on_left && !is_q_on_left) {
            return lowestCommonAncestor(root->right, p, q);
        } else {
            return root;
        }
    }
private:
    bool Covers(TreeNode* root, TreeNode* target) {
        if (root == nullptr) { return false; }
        if (root == target) { return true; }
        return Covers(root->left, target) || Covers(root->right, target);
    }
};
