#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int first = 0;
        int last = static_cast<int>(nums.size()) - 1;
        while (first <= last) {
            int middle = first + (last - first) / 2;
            if (nums[middle] == target) { return middle; }
            if (nums[first] <= nums[middle]) {  // nums[first:middle+1] is sorted
                if (nums[first] <= target && target < nums[middle]) {
                    last = middle - 1;
                } else {
                    first = middle + 1;
                }
            } else {  // nums[middle:last+1] is sorted
                if (nums[middle] < target && target <= nums[last]) {
                    first = middle + 1;
                } else {
                    last = middle - 1;
                }
            }
        }

        return -1;
    }
};
