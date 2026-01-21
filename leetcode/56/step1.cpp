#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
        std::vector<std::vector<int>> sorted_intervals(intervals);
        std::sort(sorted_intervals.begin(), sorted_intervals.end());

        std::vector<std::vector<int>> merged_intervals;

        int merged_start = sorted_intervals[0][0];
        int merged_end = sorted_intervals[0][1];
        for (size_t merging = 1; merging < sorted_intervals.size(); ++merging) {
            int merging_start = sorted_intervals[merging][0];
            int merging_end = sorted_intervals[merging][1];

            if (merged_end < merging_start) {
                merged_intervals.push_back({merged_start, merged_end});
                merged_start = merging_start;
                merged_end = merging_end;
            } else {
                merged_end = std::max(merged_end, merging_end);
            }
        }

        merged_intervals.push_back({merged_start, merged_end});
        return merged_intervals;
    }
};
