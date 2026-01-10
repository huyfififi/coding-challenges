#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        const int WATER = '0';
        const int num_rows = (int)grid.size();
        const int num_cols = (int)grid[0].size();
        const std::tuple<int, int> DIRECTIONS[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        std::vector<std::vector<bool>> visited(num_rows, std::vector<bool>(num_cols, false));

        int num_islands = 0;
        for (int row = 0; row < num_rows; ++row) {
            for (int col = 0; col < num_cols; ++col) {
                if (grid[row][col] == WATER) { continue; }
                if (visited[row][col]) { continue; }

                ++num_islands;

                std::queue<std::tuple<int, int>> area_to_explore;
                area_to_explore.push({row, col});
                while (!area_to_explore.empty()) {
                    auto [r, c] = area_to_explore.front();
                    area_to_explore.pop();

                    if (r < 0 || num_rows <= r || c < 0 || num_cols <= c) { continue; }
                    if (grid[r][c] == WATER) { continue; }
                    if (visited[r][c]) { continue; }

                    visited[r][c] = true;
                    for (auto [row_diff, col_diff] : DIRECTIONS) {
                        area_to_explore.push({r + row_diff, c + col_diff});
                    }
                }
            }
        }

        return num_islands;
    }
};
