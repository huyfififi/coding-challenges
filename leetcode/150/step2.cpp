#include <functional>
#include <map>
#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    int evalRPN(const std::vector<std::string>& tokens) {
        std::map<std::string, std::function<int(int, int)>> operator_to_function = {
            {"+", std::plus<int>()},
            {"-", std::minus<int>()},
            {"*", std::multiplies<int>()},
            {"/", std::divides<int>()},
        };

        std::stack<int> operands;
        for (const auto& token : tokens) {
            if (!operator_to_function.contains(token)) {
                operands.push(std::stoi(token));
                continue;
            }
            const auto& operator_function = operator_to_function[token];
            int right_operand = operands.top();
            operands.pop();
            int left_operand = operands.top();
            operands.pop();
            operands.push(operator_function(left_operand, right_operand));
        }
        return operands.top();
    }
};
