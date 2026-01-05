#include <set>
#include <vector>

class Solution {
public:
    bool canFinish(int numCourses, const std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> course_to_prerequisites(numCourses);
        for (const auto& course_and_prerequisite : prerequisites) {
            const int course = course_and_prerequisite[0];
            const int prerequisite = course_and_prerequisite[1];
            course_to_prerequisites[course].push_back(prerequisite);
        }

        std::set<int> visited;
        for (int course = 0; course < numCourses; ++course) {
            std::set<int> visiting;
            if (HasCycle(course, course_to_prerequisites, visiting, visited)) {
                return false;
            }
        }
        return true;
    }

private:
    bool HasCycle(
        int course,
        const std::vector<std::vector<int>>& course_to_prerequisites,
        std::set<int>& visiting,
        std::set<int>& visited) {
        if (visiting.contains(course)) {
            return true;
        }
        if (visited.contains(course)) {
            return false;
        }

        visiting.insert(course);
        for (const auto& prerequisite : course_to_prerequisites[course]) {
            if (HasCycle(prerequisite, course_to_prerequisites, visiting, visited)) {
                return true;
            }
        }
        visiting.erase(course);
        visited.insert(course);
        return false;
    }
};
