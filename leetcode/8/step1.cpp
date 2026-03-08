#include <limits>
#include <string>

class Solution {
public:
    int myAtoi(const std::string s) {
        const std::string decimal_string = "0123456789";
        const long upper_bound = std::numeric_limits<int32_t>::max();
        const long lower_bound = std::numeric_limits<int32_t>::min();

        bool positive = true;
        long result = 0;
        size_t start = 0;
        while (s[start] == ' ') { ++start; }
        if (s[start] == '-') {
            positive = false;
            ++start;
        }
        if (s[start] == '+') {
            if (!positive) { return 0; }
            ++start;
        }
        for (size_t i = start; i < s.size(); ++i) {
            char c = s[i];
            size_t digit = decimal_string.find(c);
            if (digit == -1) { break; }

            if (!positive) {
                if (result > 0) {
                    result *= -1;
                }
                result = result * 10 - digit;
                result = std::max(result, lower_bound);
            } else {
                result = result * 10 + digit;
                result = std::min(result, upper_bound);
            }
        }

        return static_cast<int>(result);
    }
};
