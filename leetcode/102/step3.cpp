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
    std::vector<std::vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> level_to_values;
        if (root == nullptr) {
            return level_to_values;
        }

        std::vector<TreeNode*> nodes{root};
        std::vector<TreeNode*> next_nodes;

        while (!nodes.empty()) {
            std::vector<int>& values = level_to_values.emplace_back();
            values.reserve(nodes.size());
            next_nodes.clear();
            next_nodes.reserve(2 * nodes.size());  // upper bound for binary tree

            for (TreeNode* node : nodes) {
                values.push_back(node->val);
                if (node->left != nullptr) {
                    next_nodes.push_back(node->left);
                }
                if (node->right != nullptr) {
                    next_nodes.push_back(node->right);
                }
            }

            nodes.swap(next_nodes);
        }

        return level_to_values;
    }
};
