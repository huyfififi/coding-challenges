#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int orangesRotting(const std::vector<std::vector<int>>& grid) {
        constexpr int kFresh = 1;
        constexpr int kRotten = 2;
        constexpr std::pair<int, int> kDeltas[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        std::vector<std::vector<int>> oranges(grid);
        const int num_rows = (int)oranges.size();
        const int num_cols = (int)oranges[0].size();

        int fresh_count = 0;
        std::queue<std::pair<int, int>> rotten_oranges;

        for (int row = 0; row < num_rows; ++row) {
            for (int col = 0; col < num_cols; ++col) {
                if (oranges[row][col] == kFresh) {
                    ++fresh_count;
                } else if (oranges[row][col] == kRotten) {
                    rotten_oranges.push({row, col});
                }
            }
        }

        int minutes_taken = 0;
        while (!rotten_oranges.empty() && fresh_count > 0) {
            int rotten_count = (int)rotten_oranges.size();
            for (int i = 0; i < rotten_count; ++i) {
                auto [row, col] = rotten_oranges.front();
                rotten_oranges.pop();

                for (auto [row_delta, col_delta] : kDeltas) {
                    int next_row = row + row_delta;
                    int next_col = col + col_delta;
                    if (next_row < 0 || num_rows <= next_row ||
                        next_col < 0 || num_cols <= next_col) {
                        continue;
                    }
                    if (oranges[next_row][next_col] != kFresh) { continue; }

                    oranges[next_row][next_col] = kRotten;
                    rotten_oranges.push({next_row, next_col});
                    --fresh_count;
                }
            }

            ++minutes_taken;
        }

        if (fresh_count > 0) { return -1; }
        return minutes_taken;
    }
};
