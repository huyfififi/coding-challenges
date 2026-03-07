#include <cstdint>
#include <string>
#include <vector>

class Solution {
public:
    bool wordBreak(const std::string& s, const std::vector<std::string>& wordDict) {
        std::vector<uint8_t> possible(s.size() + 1);
        possible[0] = 1;
        for (size_t i = 0; i < s.size(); ++i) {
            for (const auto& word : wordDict) {
                if (i + word.size() > s.size()) { continue; }
                possible[i + word.size()] |= possible[i] && !s.compare(i, word.size(), word);
            }
            if (possible[s.size()]) { return true; }
        }

        return false;
    }
};
