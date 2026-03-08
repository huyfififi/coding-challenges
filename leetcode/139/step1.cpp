#include <string>
#include <vector>

class Solution {
public:
    bool wordBreak(const std::string s, const std::vector<std::string>& word_dict) {
        std::vector<bool> reachable(s.size() + 1, false);
        reachable[0] = true;

        for (int segment_start = 0; segment_start < s.size(); ++segment_start) {
            if (!reachable[segment_start]) { continue; }

            for (const auto& word : word_dict) {
                int segment_end = segment_start + word.size();
                if (segment_end > s.size()) { continue; }
                if (!s.compare(segment_start, word.size(), word)) {
                    reachable[segment_end] = true;
                }
            }
        }

        return reachable[s.size()];
    }
};
