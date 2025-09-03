#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<std::string> token_stack;
        for (std::string token : tokens) {
            if (token != "+" && token != "-" && token != "*" && token != "/") {
                token_stack.push(token);
                continue;
            }

            int operand2 = std::stoi(token_stack.top());
            token_stack.pop();
            int operand1 = std::stoi(token_stack.top());
            token_stack.pop();

            if (token == "+") {
                token_stack.push(std::to_string(operand1 + operand2));
                continue;
            }

            if (token == "-") {
                token_stack.push(std::to_string(operand1 - operand2));
                continue;
            }

            if (token == "*") {
                token_stack.push(std::to_string(operand1 * operand2));
                continue;
            }

            token_stack.push(std::to_string(operand1 / operand2));
        }

        return std::stoi(token_stack.top());
    }
};
