#include <optional>

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return IsValidBSTHelper(root, std::nullopt, std::nullopt);
    }

private:
    bool IsValidBSTHelper(
        const TreeNode* root,
        const std::optional<int>& lower_bound,
        const std::optional<int>& upper_bound
    ) {
        if (root == nullptr) {
            return true;
        }
        if (lower_bound && root->val <= *lower_bound) {
            return false;
        }
        if (upper_bound && root->val >= *upper_bound) {
            return false;
        }
        return IsValidBSTHelper(root->left, lower_bound, root->val) &&
               IsValidBSTHelper(root->right, root->val, upper_bound);
    }
};
