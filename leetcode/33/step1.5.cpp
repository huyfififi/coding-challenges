#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int first = 0;
        int last = static_cast<int>(nums.size()) - 1;
        while (first < last) {
            int middle = first + (last - first) / 2;
            if (nums[middle] > nums[last]) {
                first = middle + 1;
            } else {
                last = middle;
            }
        }
        int min_index = first;

        first = 0;
        last = static_cast<int>(nums.size() - 1);
        if (nums[min_index] <= target && target <= nums[last]) {
            first = min_index;
        } else {
            last = min_index - 1;
        }

        while (first < last) {
            int middle = first + (last - first) / 2;
            if (nums[middle] < target) {
                first = middle + 1;
            } else {
                last = middle;
            }
        }

        if (nums[first] == target) { return first; }
        return -1;
    }
};
