#include <algorithm>
#include <chrono>
#include <set>
#include <stack>
#include <string>
#include <iostream>
#include <vector>

static const std::set<std::string> kOperatorsSet = {"+", "-", "*", "/"};
static const std::vector<std::string> kOperatorsVector = {"+", "-", "*", "/"};

class SetBasedSolution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        std::stack<int> operands;
        for (std::string token : tokens) {
            if (!kOperatorsSet.contains(token)) {
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

class VectorBasedSolution {
    public:
        int evalRPN(std::vector<std::string>& tokens) {
            std::stack<int> operands;
            for (std::string token : tokens) {
                if (std::find(kOperatorsVector.begin(), kOperatorsVector.end(), token) == kOperatorsVector.end()) {
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

int main() {
    std::vector<std::string> bestCaseRPN;
    bestCaseRPN.push_back("1");
    for (int i = 2; i <= 50; ++i) {
        bestCaseRPN.push_back(std::to_string(i));
        bestCaseRPN.push_back("+");
    }
    
    std::vector<std::string> worstCaseRPN;
    worstCaseRPN.push_back(std::to_string(33554432 * 2));
    for (int i = 2; i <= 50; ++i) {
        if (i % 2 == 0) {
            worstCaseRPN.push_back("2");
            worstCaseRPN.push_back("/");
        } else {
            worstCaseRPN.push_back("1");
            worstCaseRPN.push_back("/");
        }
    }
    
    std::cout << "Best case RPN (for linear search, operators early, only '+'): " << bestCaseRPN.size() << " elements" << std::endl;
    std::cout << "Worst case RPN (for linear search, operators late, only '/'): " << worstCaseRPN.size() << " elements" << std::endl;
    std::cout << "SetBasedSolution (best case): " << SetBasedSolution().evalRPN(bestCaseRPN) << std::endl;
    std::cout << "VectorBasedSolution (best case): " << VectorBasedSolution().evalRPN(bestCaseRPN) << std::endl;
    std::cout << "SetBasedSolution (worst case): " << SetBasedSolution().evalRPN(worstCaseRPN) << std::endl;
    std::cout << "VectorBasedSolution (worst case): " << VectorBasedSolution().evalRPN(worstCaseRPN) << std::endl;

    const int iterations = 100000;

    // Best case: Set-based
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < iterations; ++i) {
        SetBasedSolution().evalRPN(bestCaseRPN);
    }
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "\nSetBasedSolution (best case) - " << iterations << " iterations:" << std::endl;
    std::cout << "  Total time: " << duration.count() << " microseconds" << std::endl;
    std::cout << "  Average time per iteration: " << duration.count() / static_cast<double>(iterations) << " microseconds" << std::endl;

    // Best case: Vector-based
    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < iterations; ++i) {
        VectorBasedSolution().evalRPN(bestCaseRPN);
    }
    end = std::chrono::high_resolution_clock::now();
    duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "\nVectorBasedSolution (best case) - " << iterations << " iterations:" << std::endl;
    std::cout << "  Total time: " << duration.count() << " microseconds" << std::endl;
    std::cout << "  Average time per iteration: " << duration.count() / static_cast<double>(iterations) << " microseconds" << std::endl;

    // Worst case: Set-based
    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < iterations; ++i) {
        SetBasedSolution().evalRPN(worstCaseRPN);
    }
    end = std::chrono::high_resolution_clock::now();
    duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "\nSetBasedSolution (worst case) - " << iterations << " iterations:" << std::endl;
    std::cout << "  Total time: " << duration.count() << " microseconds" << std::endl;
    std::cout << "  Average time per iteration: " << duration.count() / static_cast<double>(iterations) << " microseconds" << std::endl;

    // Worst case: Vector-based
    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < iterations; ++i) {
        VectorBasedSolution().evalRPN(worstCaseRPN);
    }
    end = std::chrono::high_resolution_clock::now();
    duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "\nVectorBasedSolution (worst case) - " << iterations << " iterations:" << std::endl;
    std::cout << "  Total time: " << duration.count() << " microseconds" << std::endl;
    std::cout << "  Average time per iteration: " << duration.count() / static_cast<double>(iterations) << " microseconds" << std::endl;

    /*
    Best case RPN (for linear search, operators early, only '+'): 99 elements
    Worst case RPN (for linear search, operators late, only '/'): 99 elements
    SetBasedSolution (best case): 1275
    VectorBasedSolution (best case): 1275
    SetBasedSolution (worst case): 2
    VectorBasedSolution (worst case): 2

    SetBasedSolution (best case) - 100000 iterations:
      Total time: 228406 microseconds
      Average time per iteration: 2.28406 microseconds

    VectorBasedSolution (best case) - 100000 iterations:
      Total time: 121551 microseconds
      Average time per iteration: 1.21551 microseconds

    SetBasedSolution (worst case) - 100000 iterations:
      Total time: 195376 microseconds
      Average time per iteration: 1.95376 microseconds

    VectorBasedSolution (worst case) - 100000 iterations:
      Total time: 190418 microseconds
      Average time per iteration: 1.90418 microseconds
    */

    return 0;
}
