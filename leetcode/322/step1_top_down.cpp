#include <algorithm>
#include <vector>

class Solution {
public:
    int coinChange(const std::vector<int>& coins, int amount) {
        const int unreachable = amount + 1;
        std::vector<int> min_nums(amount + 1, unreachable);
        min_nums[0] = 0;
        return ComputeMinCoins(coins, min_nums, amount, unreachable);
    }

private:
    int ComputeMinCoins(const std::vector<int>& coins,
                        std::vector<int>& min_nums,
                        int amount,
                        int unreachable) {
        if (min_nums[amount] != unreachable) {
            return min_nums[amount];
        }

        int min_num = unreachable;
        for (int coin : coins) {
            if (amount < coin) {
                continue;
            }
            int result = ComputeMinCoins(coins, min_nums, amount - coin, unreachable);
            if (result == -1) {
                continue;
            }
            min_num = std::min(min_num, result + 1);
        }

        if (min_num == unreachable) {
            min_nums[amount] = -1;
        } else {
            min_nums[amount] = min_num;
        }
        return min_nums[amount];
    }
};
