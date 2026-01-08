#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        std::vector<int> prefix_products(nums.size(), 1);
        for (int i = 1; i < nums.size(); ++i) {
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1];
        }
        std::vector<int> suffix_products(nums.size(), 1);
        for (int i = nums.size() - 2; 0 <= i; --i) {
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1];
        }

        std::vector<int> products_except_self(nums.size());
        for (int i = 0; i < nums.size(); ++i) {
            products_except_self[i] = prefix_products[i] * suffix_products[i];
        }
        return products_except_self;
    }
};
