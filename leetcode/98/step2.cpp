#include <optional>

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return IsValidBSTHelper(root, std::nullopt, std::nullopt);
    }

private:
    bool IsValidBSTHelper(
        const TreeNode* node,
        const std::optional<int>& lower_bound,
        const std::optional<int>& upper_bound
    ) {
        if (node == nullptr) {
            return true;
        }
        if (lower_bound && node->val <= *lower_bound) {
            return false;
        }
        if (upper_bound && node->val >= *upper_bound) {
            return false;
        }

        return IsValidBSTHelper(node->left, lower_bound, node->val) &&
               IsValidBSTHelper(node->right, node->val, upper_bound);
    }
};
