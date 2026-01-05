#include <algorithm>
#include <vector>

class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
        std::vector<int> min_counts(amount + 1, -1);
        min_counts[0] = 0;

        for (int total = 1; total < amount + 1; ++total) {
            for (const auto& coin : coins) {
                if (total - coin < 0) {
                    continue;
                }
                if (min_counts[total - coin] == -1) {
                    continue;
                }

                if (min_counts[total] == -1) {
                    min_counts[total] = min_counts[total - coin] + 1;
                } else {
                    min_counts[total] = std::min(min_counts[total], min_counts[total - coin] + 1);
                }
            }
        }

        return min_counts[amount];
    }
};
