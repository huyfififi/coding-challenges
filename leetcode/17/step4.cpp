#include <map>
#include <utility>
#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        if (digits.empty()) { return {}; }

        std::map<char, std::vector<char>> digit_to_characters = {
            {'2', {'a', 'b', 'c'}},
            {'3', {'d', 'e', 'f'}},
            {'4', {'g', 'h', 'i'}},
            {'5', {'j', 'k', 'l'}},
            {'6', {'m', 'n', 'o'}},
            {'7', {'p', 'q', 'r', 's'}},
            {'8', {'t', 'u', 'v'}},
            {'9', {'w', 'x', 'y', 'z'}},
        };

        std::vector<std::string> possible_combinations;
        std::stack<std::pair<int, std::vector<char>>> combinations_in_progress;
        combinations_in_progress.push({0, {}});
        while (!combinations_in_progress.empty()) {
            auto top = std::move(combinations_in_progress.top());
            combinations_in_progress.pop();
            auto [digit_index, combination_in_progress] = std::move(top);

            if (digit_index == digits.size()) {
                possible_combinations.emplace_back(
                    combination_in_progress.begin(), combination_in_progress.end()
                );
                continue;
            }

            for (char possible_character : digit_to_characters[digits[digit_index]]) {
                std::vector<char> next_combination(combination_in_progress);
                next_combination.push_back(possible_character);
                combinations_in_progress.emplace(digit_index + 1, std::move(next_combination));
            }
        }

        return possible_combinations;
    }
};
