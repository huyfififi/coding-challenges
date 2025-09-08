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

class Solution {
private:
    Node* CloneGraphHelper(Node* node, std::map<Node*, Node*>& node_to_clone) {
        if (node_to_clone.contains(node)) {
            return node_to_clone[node];
        }

        Node* clone = new Node(node->val);
        node_to_clone[node] = clone;

        for (Node* neighbor : node->neighbors) {
            Node* neighbor_clone = CloneGraphHelper(neighbor, node_to_clone);
            clone->neighbors.push_back(neighbor_clone);
        }

        return clone;
    }

public:
    Node* cloneGraph(Node* start) {
        if (start == nullptr) {
            return nullptr;
        }

        std::map<Node*, Node*> node_to_clone;
        return CloneGraphHelper(start, node_to_clone);
        
    }
};
