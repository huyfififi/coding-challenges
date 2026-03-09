#include <string>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        int max_start = 0;
        int max_end = 0;
        int max_length = 0;

        for (int start = 0; start < s.size(); ++start) {
            for (int end = start; end < s.size(); ++end) {
                if (end - start < max_length) { continue; }

                int left = start;
                int right = end;
                while (left < right) {
                    if (s[left] != s[right]) {
                        break;
                    }
                    ++left;
                    --right;
                }

                if (left >= right) {
                    max_start = start;
                    max_end = end;
                    max_length = end - start;
                }
            }
        }

        return s.substr(max_start, max_end - max_start + 1);
    }
};
