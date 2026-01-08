#include <algorithm>
#include <stack>
#include <tuple>

class MinStack {
public:
    void push(int val) {
        if (num_and_prefix_min.empty()) {
            num_and_prefix_min.push({val, val});
        } else {
            int prev_prefix_min = getMin();
            num_and_prefix_min.push({val, std::min(val, prev_prefix_min)});
        }
    }
    
    void pop() {
        num_and_prefix_min.pop();
    }
    
    int top() const {
        return std::get<0>(num_and_prefix_min.top());
    }
    
    int getMin() const {
        return std::get<1>(num_and_prefix_min.top());
    }
private:
    std::stack<std::tuple<int, int>> num_and_prefix_min;
};
