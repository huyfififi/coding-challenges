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
#include <functional>
#include <map>

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) {
            return nullptr;
        }

        std::map<Node*, Node*> node_to_clone;

        std::function<Node* (Node*)> clone_graph = [&](Node* original) -> Node* {
            if (node_to_clone.contains(original)) {
                return node_to_clone[original];
            }

            Node* clone = new Node(original->val);
            node_to_clone[original] = clone;
            for (Node* neighbor : original->neighbors) {
                Node* neighbor_clone = clone_graph(neighbor);
                clone->neighbors.push_back(neighbor_clone);
            }
            return clone;
        };

        return clone_graph(node);
    }
};
