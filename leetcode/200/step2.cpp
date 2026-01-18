#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int numIslands(const std::vector<std::vector<char>>& grid) {
        constexpr char kWater = '0';
        const int num_rows = (int)grid.size();
        const int num_cols = (int)grid[0].size();

        int num_islands = 0;
        std::vector<std::vector<bool>> visited(num_rows, std::vector<bool>(num_cols));

        for (int row = 0; row < num_rows; ++row) {
            for (int col = 0; col < num_cols; ++col) {
                if (grid[row][col] == kWater) { continue; }
                if (visited[row][col]) { continue; }

                ++num_islands;

                std::queue<std::pair<int, int>> area_to_visit;
                area_to_visit.push({row, col});
                while (!area_to_visit.empty()) {
                    auto [r, c] = area_to_visit.front();
                    area_to_visit.pop();
                    if (r < 0 || num_rows <= r ||
                        c < 0 || num_cols <= c) {
                        continue;
                    }
                    if (grid[r][c] == kWater) { continue; }
                    if (visited[r][c]) { continue; }

                    area_to_visit.push({r + 1, c});
                    area_to_visit.push({r - 1, c});
                    area_to_visit.push({r, c + 1});
                    area_to_visit.push({r, c - 1});
                    visited[r][c] = true;
                }
            }
        }

        return num_islands;
    }
};
