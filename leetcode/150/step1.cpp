#include <set>
#include <stack>
#include <string>

static const std::set<std::string> kOperators = {"+", "-", "*", "/"};

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> operands;
        for (std::string token : tokens) {
            if (!kOperators.contains(token)) {
                operands.push(std::stoi(token));
                continue;
            }

            int second_operand = operands.top();
            operands.pop();
            int first_operand = operands.top();
            operands.pop();

            if (token == "+") {
                operands.push(first_operand + second_operand);
                continue;
            }
            if (token == "-") {
                operands.push(first_operand - second_operand);
                continue;
            }
            if (token == "*") {
                operands.push(first_operand * second_operand);
                continue;
            }
            if (token == "/") {
                operands.push(first_operand / second_operand);
            }
        }

        return operands.top();
    }
};
