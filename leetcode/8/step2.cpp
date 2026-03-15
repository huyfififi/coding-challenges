#include <cctype>
#include <cstdint>
#include <limits>
#include <string>

class Solution {
public:
    int myAtoi(std::string s) {
        const int int_max = std::numeric_limits<int32_t>::max();
        const int int_min = std::numeric_limits<int32_t>::min();

        auto it = s.begin();
        while (it != s.end() && std::isspace(static_cast<unsigned char>(*it))) {
            ++it;
        }

        bool is_positive = true;
        if (it != s.end() && (*it == '+' || *it == '-')) {
            is_positive &= *it == '+';
            ++it;
        }

        int integer = 0;
        for (; it != s.end(); ++it) {
            if (!std::isdigit(static_cast<unsigned char>(*it))) {
                return integer;
            }

            int digit = *it - '0';
            if (is_positive) {
                // integer * 10 + digit > int_max
                if ((int_max - digit) / 10 < integer) {
                    return int_max;
                }
                integer = integer * 10 + digit;
            } else {
                // integer * 10 - digit < int_min
                if ((int_min + digit) / 10 > integer) {
                    return int_min;
                }
                integer = integer * 10 - digit;
            }
        }

        return integer;
    }
};
