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
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) { return {}; }

        std::vector<int> rightmost_values;
        std::vector<TreeNode*> nodes{root};
        while (!nodes.empty()) {
            rightmost_values.push_back(nodes.back()->val);

            std::vector<TreeNode*> next_nodes;
            for (TreeNode* node : nodes) {
                if (node->left != nullptr) {
                    next_nodes.push_back(node->left);
                }
                if (node->right != nullptr) {
                    next_nodes.push_back(node->right);
                }
            }

            std::swap(nodes, next_nodes);
        }

        return rightmost_values;
    }
};
