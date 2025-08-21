#include <chrono>
#include <iostream>
#include <cstring>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
    ~TreeNode() {
        delete left;
        delete right;
    }

    int CountNodes() {
        int count = 1;
        if (left != nullptr) {
            count += left->CountNodes();
        }
        if (right != nullptr) {
            count += right->CountNodes();
        }
        return count;
    }
};

// imitate LeetCode's input range: The number of nodes in the tree is in the range [0, 2000].
// 2^11 - 1 = 2047 ~= 2000
TreeNode* CreateCompleteBT(int height = 11) {
    if (height == 0) {
        return nullptr;
    }
    return new TreeNode(height, CreateCompleteBT(height - 1), CreateCompleteBT(height - 1));
}

class Solution {
public:
    std::vector<std::vector<int>> levelOrderWithReserveLevelValues(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }

        std::vector<std::vector<int>> level_to_values;
        std::vector<TreeNode*> nodes{root};

        while (!nodes.empty()) {
            std::vector<int>& values = level_to_values.emplace_back();
            values.reserve(nodes.size());
            std::vector<TreeNode*> next_nodes;

            for (TreeNode* node : nodes) {
                values.push_back(node->val);
                if (node->left != nullptr) {
                    next_nodes.push_back(node->left);
                }
                if (node->right != nullptr) {
                    next_nodes.push_back(node->right);
                }
            }

            nodes.swap(next_nodes);
        }

        return level_to_values;
    }

    std::vector<std::vector<int>> levelOrderWithoutReserveLevelValues(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }

        std::vector<std::vector<int>> level_to_values;
        std::vector<TreeNode*> nodes{root};

        while (!nodes.empty()) {
            std::vector<int>& values = level_to_values.emplace_back();
            std::vector<TreeNode*> next_nodes;

            for (TreeNode* node : nodes) {
                values.push_back(node->val);
                if (node->left != nullptr) {
                    next_nodes.push_back(node->left);
                }
                if (node->right != nullptr) {
                    next_nodes.push_back(node->right);
                }
            }
            nodes.swap(next_nodes);
        }

        return level_to_values;
    }

    int GetTotalCopyLevelOrderWithoutReserveLevelValues(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        std::vector<std::vector<int>> level_to_values;
        std::vector<TreeNode*> nodes{root};

        int total_copy = 0;
        while (!nodes.empty()) {
            std::vector<int>& values = level_to_values.emplace_back();
            std::vector<TreeNode*> next_nodes;

            for (TreeNode* node : nodes) {
                if (values.size() >= values.capacity()) {
                    total_copy += values.size();
                }

                values.push_back(node->val);

                if (node->left != nullptr) {
                    next_nodes.push_back(node->left);
                }
                if (node->right != nullptr) {
                    next_nodes.push_back(node->right);
                }
            }
            nodes.swap(next_nodes);
        }

        return total_copy;
    }
};

void TestPureIntCopy() {
    const int count = 1000000;
    const int size = 1000;
    int *src = new int[size];
    int *dst = new int[size];

    for (int i = 0; i < size; i++) {
        src[i] = i;
    }

    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < count; i++) {
        memcpy(dst, src, size * sizeof(int));
    }
    auto end = std::chrono::high_resolution_clock::now();
    // -O0: Time taken: 65661416ns
    std::cout << "Time taken: " << std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count() << "ns" << std::endl;
    float average_time_per_iteration_ns = static_cast<float>(std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count()) / count;
    // -O0: Average time per iteration: 65.6614ns
    // -O3: Average time per iteration: 8.3e-05ns
    std::cout << "Average time per iteration: " << average_time_per_iteration_ns << "ns" << std::endl;
    const int CLOCK_RATE_PER_NANOSECOND = 3; // 3e9 cycles per second * 1e-9 seconds per nanosecond
    const float CLOCK_CYCLES_PER_ITERATION = average_time_per_iteration_ns * CLOCK_RATE_PER_NANOSECOND;
    float clock_cycles_per_int = CLOCK_CYCLES_PER_ITERATION / size;
    // -O0: Clock cycles per int: 0.196984
    // -O3: Clock cycles per int: 2.49e-07
    std::cout << "Clock cycles per int: " << clock_cycles_per_int << std::endl;

    delete[] src;
    delete[] dst;
}

void TestLevelOrderWithReserveLevelValues() {
    TreeNode* root = CreateCompleteBT();
    // Number of nodes: 2047
    std::cout << "Number of nodes: " << root->CountNodes() << std::endl;

    int count = 1000000;

    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < count; i++) {
        Solution().levelOrderWithReserveLevelValues(root);
    }
    auto end = std::chrono::high_resolution_clock::now();
    // -O0: Time taken with reserve: 71284419us
    // -O3: Time taken with reserve: 5424370us
    std::cout << "Time taken with reserve: " << std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() << "us" << std::endl;
    // -O0: Average time per iteration with reserve: 71.2844us
    // -O3: Average time per iteration with reserve: 5.42437us
    float average_time_per_iteration_with_reserve = static_cast<float>(std::chrono::duration_cast<std::chrono::microseconds>(end - start).count()) / count;
    std::cout << "Average time per iteration with reserve: " << average_time_per_iteration_with_reserve << "us" << std::endl;

    start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < count; i++) {
        Solution().levelOrderWithoutReserveLevelValues(root);
    }
    end = std::chrono::high_resolution_clock::now();
    // -O0: Time taken without reserve: 76226269us
    // -O3: Time taken without reserve: 6664478us
    std::cout << "Time taken without reserve: " << std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() << "us" << std::endl;
    // -O0: Average time per iteration without reserve: 76.2263us
    // -O3: Average time per iteration without reserve: 6.66448us
    float average_time_per_iteration_without_reserve = static_cast<float>(std::chrono::duration_cast<std::chrono::microseconds>(end - start).count()) / count;
    std::cout << "Average time per iteration without reserve: " << average_time_per_iteration_without_reserve << "us" << std::endl;

    float additional_time_per_iteration_us = average_time_per_iteration_without_reserve - average_time_per_iteration_with_reserve;
    // -O0: Additional time per iteration: 4.94186us
    // -O3: Additional time per iteration: 1.24011us
    std::cout << "Additional time per iteration: " << additional_time_per_iteration_us << "us" << std::endl;

    int total_copy = Solution().GetTotalCopyLevelOrderWithoutReserveLevelValues(root);
    // Total copy: 2036
    std::cout << "Total copy: " << total_copy << std::endl;

    const int CLOCK_RATE_PER_MICROSECOND = 3.0e9 / 1e6;
    const float CLOCK_CYCLES_IN_ADDITIONAL_TIME = additional_time_per_iteration_us * CLOCK_RATE_PER_MICROSECOND;
    float clock_cycles_per_int = CLOCK_CYCLES_IN_ADDITIONAL_TIME / total_copy;
    // -O0: Clock cycles per int: 7.28171
    // -O3: Clock cycles per int: 1.82727 (close to the theoretical value 4 bytes (32 bits) / 8 bytes (64 bits) per cycle = 0.5)
    std::cout << "Clock cycles per int: " << clock_cycles_per_int << std::endl;

    delete root;
}

// clang++ comparison.cpp -O0
// clang++ comparison.cpp -O3
int main() {
    TestPureIntCopy();
    TestLevelOrderWithReserveLevelValues();
    return 0;
}
