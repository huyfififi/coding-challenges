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
        if (root == nullptr) {
            return level_to_values;
        }

        std::queue<TreeNode*> nodes;
        nodes.push(root);
        while (!nodes.empty()) {
            std::vector<int>& values = level_to_values.emplace_back();
            std::queue<TreeNode*> next_nodes;

            while (!nodes.empty()) {
                TreeNode* node = nodes.front();
                nodes.pop();
                if (node->left != nullptr) {
                    next_nodes.push(node->left);
                }
                if (node->right != nullptr) {
                    next_nodes.push(node->right);
                }
                values.push_back(node->val);
            }
            nodes.swap(next_nodes);
        }
        return level_to_values;
    }
};
