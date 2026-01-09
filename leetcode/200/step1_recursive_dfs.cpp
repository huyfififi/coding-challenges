#include <tuple>
#include <vector>

class Solution {
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        const int num_rows = (int)grid.size();
        const int num_cols = (int)grid[0].size();
        std::vector<std::vector<bool>> visited(num_rows, std::vector<bool>(num_cols, false));

        int num_islands = 0;
        for (int row = 0; row < num_rows; ++row) {
            for (int col = 0; col < num_cols; ++col) {
                if (grid[row][col] == WATER) {
                    continue;
                }
                if (visited[row][col]) {
                    continue;
                }

                ++num_islands;
                ExploreIsland(row, col, grid, visited);
            }
        }

        return num_islands;
    }

private:
    static const char WATER = '0';
    void ExploreIsland(
        int row,
        int col,
        const std::vector<std::vector<char>>& grid,
        std::vector<std::vector<bool>>& visited
    ) {
        if (row < 0 || (int)grid.size() <= row || col < 0 || (int)grid[0].size() <= col) {
            return;
        }
        if (visited[row][col]) {
            return;
        }
        if (grid[row][col] == WATER) {
            return;
        }

        visited[row][col] = true;
        const std::tuple<int, int> directions[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (auto [row_diff, col_diff] : directions) {
            ExploreIsland(row + row_diff, col + col_diff, grid, visited);
        }
    }
};
