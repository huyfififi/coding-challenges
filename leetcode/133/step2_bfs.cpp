/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
#include <map>
#include <queue>

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }

        std::map<Node*, Node*> node_to_clone;
        node_to_clone[node] = new Node(node->val);
        std::queue<Node*> nodes;
        nodes.push(node);

        while (!nodes.empty()) {
            Node* original = nodes.front();
            nodes.pop();
            Node* clone = node_to_clone[original];

            for (Node* neighbor : original->neighbors) {
                Node* neighbor_clone = node_to_clone[neighbor];
                if (neighbor_clone == nullptr) {
                    neighbor_clone = new Node(neighbor->val);
                    node_to_clone[neighbor] = neighbor_clone;
                    nodes.push(neighbor);
                }

                clone->neighbors.push_back(neighbor_clone);
            }
        }

        return node_to_clone[node];
    }
};
