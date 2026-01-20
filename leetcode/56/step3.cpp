#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> merge(const std::vector<std::vector<int>>& intervals) {
        std::vector<std::vector<int>> sorted_intervals(intervals);
        std::sort(sorted_intervals.begin(), sorted_intervals.end());

        std::vector<std::vector<int>> merged_intervals;
        std::vector<int> last_interval = sorted_intervals.front();
        for (size_t i = 1; i < sorted_intervals.size(); ++i) {
            std::vector<int> interval = sorted_intervals[i];
            if (last_interval[1] < interval[0]) {
                merged_intervals.push_back(last_interval);
                last_interval = interval;
            } else {
                last_interval[1] = std::max(last_interval[1], interval[1]);
            }
        }

        merged_intervals.push_back(last_interval);
        return merged_intervals;
    }
};
