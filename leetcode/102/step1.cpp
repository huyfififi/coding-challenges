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
#include <queue>
#include <vector>


class Solution {
public:
    std::vector<std::vector<int>> levelOrder(TreeNode* root) {
        std::queue<TreeNode*> curr_queue;
        curr_queue.push(root);
        std::vector<std::vector<int>> answer;
        while (true) {
            std::vector<int> level_result;
            std::queue<TreeNode*> next_queue;
            while (!curr_queue.empty()) {
                TreeNode* node = curr_queue.front();
                curr_queue.pop();
                if (node == nullptr) {
                    continue;
                }

                level_result.push_back(node->val);
                next_queue.push(node->left);
                next_queue.push(node->right);
            }

            if (level_result.empty()) {
                break;
            }

            answer.push_back(level_result);
            curr_queue.swap(next_queue);
        }
        return answer;
    }
};
