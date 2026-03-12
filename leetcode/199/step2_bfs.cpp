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
#include <cstddef>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) { return {}; }

        std::vector<int> rightmost_values;
        std::vector<TreeNode*> nodes{root};
        while (!nodes.empty()) {
            std::vector<TreeNode*> next_nodes;
            for (std::size_t i = 0; i < nodes.size(); ++i) {
                if (i == nodes.size() - 1) {
                    rightmost_values.push_back(nodes[i]->val);
                }
                if (nodes[i]->left != nullptr) {
                    next_nodes.push_back(nodes[i]->left);
                }
                if (nodes[i]->right != nullptr) {
                    next_nodes.push_back(nodes[i]->right);
                }
            }

            std::swap(nodes, next_nodes);
        }

        return rightmost_values;
    }
};
