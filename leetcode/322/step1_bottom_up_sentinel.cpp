#include <algorithm>
#include <vector>

class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
        const int impossible = amount + 1;
        std::vector<int> min_num_coins(amount + 1, impossible);
        min_num_coins[0] = 0;

        for (int total = 1; total < amount + 1; ++total) {
            for (int coin : coins) {
                if (total < coin) {
                    continue;
                }
                min_num_coins[total] = std::min(min_num_coins[total], min_num_coins[total - coin] + 1);
            }
        }

        if (min_num_coins[amount] == impossible) {
            return -1;
        }
        return min_num_coins[amount];
    }
};
