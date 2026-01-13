#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int orangesRotting(const std::vector<std::vector<int>>& grid) {
        constexpr int kFresh = 1;
        constexpr int kRotten = 2;
        constexpr std::pair<int, int> kDirections[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        std::vector<std::vector<int>> oranges(grid);
        const int num_rows = (int)oranges.size();
        const int num_cols = (int)oranges[0].size();

        std::queue<std::pair<int, int>> rotten_oranges;
        for (int row = 0; row < num_rows; ++row) {
            for (int col = 0; col < num_cols; ++col) {
                if (oranges[row][col] == kRotten) {
                    rotten_oranges.push({row, col});
                }
            }
        }

        int minutes = 0;
        while (!rotten_oranges.empty()) {
            int num_rotten_oranges = (int)rotten_oranges.size();
            bool any_orange_rots = false;
            for (int i = 0; i < num_rotten_oranges; ++i) {
                auto [row, col] = rotten_oranges.front();
                rotten_oranges.pop();

                for (auto [row_diff, col_diff] : kDirections) {
                    int next_row = row + row_diff;
                    int next_col = col + col_diff;
                    if (next_row < 0 || num_rows <= next_row ||
                        next_col < 0 || num_cols <= next_col) {
                        continue;
                    }
                    if (oranges[next_row][next_col] != kFresh) { continue; }
                    rotten_oranges.push({next_row, next_col});
                    oranges[next_row][next_col] = kRotten;
                    any_orange_rots = true;
                }
            }

            if (any_orange_rots) { ++minutes; }
        }

        for (int row = 0; row < num_rows; ++row) {
            for (int col = 0; col < num_cols; ++col) {
                if (oranges[row][col] == kFresh) { return -1; }
            }
        }
        return minutes;
    }
};
