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
#include <queue>


class Solution {
public:
    std::vector<std::vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> level_to_values;
        if (!root) {
            return level_to_values;
        }

        std::queue<TreeNode*> nodes;
        nodes.push(root);
        while (!nodes.empty()) {
            const size_t n = nodes.size();
            level_to_values.emplace_back();
            std::vector<int>& values = level_to_values.back();
            values.reserve(n);

            for (size_t i = 0; i < n; ++i) {
                TreeNode* node = nodes.front();
                nodes.pop();
                values.push_back(node->val);
                if (node->left) {
                    nodes.push(node->left);
                }
                if (node->right) {
                    nodes.push(node->right);
                }
            }
        }

        return level_to_values;
    }
};
