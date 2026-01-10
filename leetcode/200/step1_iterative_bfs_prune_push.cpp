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
                visited[row][col] = true;

                std::queue<std::tuple<int, int>> area_to_explore;
                area_to_explore.push({row, col});
                while (!area_to_explore.empty()) {
                    auto [r, c] = area_to_explore.front();
                    area_to_explore.pop();

                    for (auto [row_diff, col_diff] : DIRECTIONS) {
                        int next_r = r + row_diff;
                        int next_c = c + col_diff;
                        if (next_r < 0 || num_rows <= next_r || next_c < 0 || num_cols <= next_c) { continue; }
                        if (grid[next_r][next_c] == WATER) { continue; }
                        if (visited[next_r][next_c]) { continue; }

                        area_to_explore.push({next_r, next_c});
                        visited[next_r][next_c] = true;
                    }
                }
            }
        }

        return num_islands;
    }
};
