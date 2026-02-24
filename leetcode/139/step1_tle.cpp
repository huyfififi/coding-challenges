#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    bool wordBreak(const std::string s, const std::vector<std::string>& wordDict) {
        std::stack<int> substring_starts;
        substring_starts.push(0);
        while (!substring_starts.empty()) {
            int substring_start = substring_starts.top();
            if (substring_start == s.size()) { return true; }
            substring_starts.pop();

            for (const auto& word : wordDict) {
                int substring_end = substring_start + word.size();
                if (substring_end > s.size()) { continue; }
                if (!s.compare(substring_start, word.size(), word)) {
                    substring_starts.push(substring_end);
                }
            }
        }

        return false;
    }
};
