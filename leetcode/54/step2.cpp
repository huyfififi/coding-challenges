#include <cstdint>
#include <vector>

class Solution {
public:
    std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
        int num_rows = static_cast<int>(matrix.size());
        int num_cols = static_cast<int>(matrix[0].size());

        std::vector<std::vector<uint8_t>> visited(num_rows, std::vector<uint8_t>(num_cols));
        int row = 0;
        int col = 0;
        int row_delta = 0;
        int col_delta = 1;
        std::vector<int> result;
        for (int i = 0; i < num_rows * num_cols; ++i) {
            result.push_back(matrix[row][col]);
            visited[row][col] = 1;

            int next_row = row + row_delta;
            int next_col = col + col_delta;
            if (
                !(0 <= next_row && next_row < num_rows && 0 <= next_col && next_col < num_cols)
                || visited[next_row][next_col]
            ) {
                int new_row_delta = col_delta;
                int new_col_delta = -row_delta;
                row_delta = new_row_delta;
                col_delta = new_col_delta;
                next_row = row + row_delta;
                next_col = col + col_delta;
            }

            row = next_row;
            col = next_col;
        }

        return result;
    }
};
