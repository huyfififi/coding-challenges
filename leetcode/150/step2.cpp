#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> nums;
        for (const std::string& token : tokens) {
            if (token != "+" && token != "-" && token != "*" && token != "/") {
                nums.push(std::stoi(token));
                continue;
            }

            int right_operand = nums.top();
            nums.pop();
            int left_operand = nums.top();
            nums.pop();

            if (token == "+") {
                nums.push(left_operand + right_operand);
                continue;
            }

            if (token == "-") {
                nums.push(left_operand - right_operand);
                continue;
            }

            if (token == "*") {
                nums.push(left_operand * right_operand);
                continue;
            }

            nums.push(left_operand / right_operand);
        }

        return nums.top();
    }
};
