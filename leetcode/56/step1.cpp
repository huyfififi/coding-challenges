#include <algorithm>
#include <vector>


class Solution {
public:
    std::vector<std::vector<int>> merge(std::vector<std::vector<int>>& intervals) {
        std::vector<std::vector<int>> sorted_intervals(intervals);
        std::sort(sorted_intervals.begin(), sorted_intervals.end());

        std::vector<std::vector<int>> merged_intervals;

        int merging_start = sorted_intervals[0][0];
        int merging_end = sorted_intervals[0][1];
        size_t checking = 1;
        while (checking < static_cast<int>(sorted_intervals.size())) {
            int checking_start = sorted_intervals[checking][0];
            int checking_end = sorted_intervals[checking][1];
            if (merging_end < checking_start) {
                merged_intervals.push_back({merging_start, merging_end});
                merging_start = checking_start;
                merging_end = checking_end;
                ++checking;
                continue;
            }

            merging_end = std::max(merging_end, checking_end);
            ++checking;
        }

        merged_intervals.push_back({merging_start, merging_end});
        return merged_intervals;
    }
};
