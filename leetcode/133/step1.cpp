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
        std::function<Node* (Node*)> CloneGraphHelper = [&](Node* node) -> Node* {
            if (node_to_clone.contains(node)) {
                return node_to_clone[node];
            }

            Node* clone_node = new Node(node->val);
            node_to_clone[node] = clone_node;
            for (Node* neighbor : node->neighbors) {
                Node* clone_neighbor = CloneGraphHelper(neighbor);
                clone_node->neighbors.push_back(clone_neighbor);
            }
            return clone_node;
        };

        CloneGraphHelper(node);
        return node_to_clone[node];
    }
};
