#include <functional>
#include <map>
#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    int evalRPN(const std::vector<std::string>& tokens) {
        static const std::map<std::string, std::function<int(int, int)>> operator_to_function = {
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

            const auto& operator_function = operator_to_function.at(token);
            int rhs = operands.top();
            operands.pop();
            int lhs = operands.top();
            operands.pop();
            operands.push(operator_function(lhs, rhs));
        }

        return operands.top();
    }
};
