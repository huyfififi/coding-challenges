#include <cstdint>
#include <string>
#include <vector>

class Solution {
public:
    bool wordBreak(const std::string& s, const std::vector<std::string>& wordDict) {
        std::vector<uint8_t> divisible(s.size() + 1);
        divisible[0] = 1;

        for (size_t i = 0; i < s.size(); ++i) {
            if (!divisible[i]) { continue; }
            for (const auto& word : wordDict) {
                if (i + word.size() > s.size()) { continue; }
                if (!s.compare(i, word.size(), word)) {
                    divisible[i + word.size()] = 1; 
                }
            }
        }

        return divisible[s.size()];
    }
};
