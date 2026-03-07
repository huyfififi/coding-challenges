#include <cstdint>
#include <vector>

class Solution {
public:
    bool canPartition(const std::vector<int>& nums) {
        int total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        if (total_sum % 2 == 1) { return false; }

        int half_sum = total_sum / 2;
        std::vector<uint8_t> possible(half_sum + 1);
        possible[0] = true;
        for (int num : nums) {
            for (int sum = half_sum; sum >= num; --sum) {
                possible[sum] |= possible[sum - num];
                if (sum == half_sum && possible[half_sum]) {
                    return true;
                }
            }
        }

        return false;
    }
};
