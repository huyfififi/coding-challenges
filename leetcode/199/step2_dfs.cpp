/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <vector>

class Solution {
public:
    std::vector<int> rightSideView(TreeNode* root) {
        std::vector<int> rightmost_values;
        TraverseAndStoreRightmost(root, 0, rightmost_values);
        return rightmost_values;
    }
private:
    void TraverseAndStoreRightmost(
        TreeNode* node, int depth, std::vector<int>& rightmost_values
    ) {
        if (node == nullptr) { return; }
        if (depth == static_cast<int>(rightmost_values.size())) {
            rightmost_values.push_back(node->val);
        }
        TraverseAndStoreRightmost(node->right, depth + 1, rightmost_values);
        TraverseAndStoreRightmost(node->left, depth + 1, rightmost_values);
    }
};
