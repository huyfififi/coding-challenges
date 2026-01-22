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
    bool Covers(const TreeNode* root, const TreeNode* node) {
        if (root == nullptr) { return false; }
        if (root == node) { return true; }
        return Covers(root->left, node) || Covers(root->right, node);
    }
};
