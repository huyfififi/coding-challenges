#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> merge(const std::vector<std::vector<int>>& intervals) {
        std::vector<std::vector<int>> sorted_intervals(intervals);
        std::sort(sorted_intervals.begin(), sorted_intervals.end());

        std::vector<std::vector<int>> merged_intervals;
        merged_intervals.push_back(sorted_intervals.front());
        for (const auto& interval : sorted_intervals) {
            if (merged_intervals.back()[1] < interval[0]) {
                merged_intervals.push_back(interval);
            } else {
                merged_intervals.back()[1] = std::max(merged_intervals.back()[1], interval[1]);
            }
        }
        return merged_intervals;
    }
};
