#include <functional>
#include <numeric>
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        std::vector<int> prefix_products(nums.size(), 1);
        std::partial_sum(
            nums.begin(),
            nums.end() - 1,
            prefix_products.begin() + 1,
            std::multiplies<int>()
        );

        std::vector<int> suffix_products(nums.size(), 1);
        std::partial_sum(
            nums.rbegin(),
            nums.rend() - 1,
            suffix_products.rbegin() + 1,
            std::multiplies<int>()
        );

        std::vector<int> products_except_self(nums.size());
        for (int i = 0; i < nums.size(); ++i) {
            products_except_self[i] = prefix_products[i] * suffix_products[i];
        }
        return products_except_self;
    }
};
