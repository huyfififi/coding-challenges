#include <set>
#include <vector>

class Solution {
public:
    bool canFinish(int numCourses, const std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> course_prerequisites(numCourses);
        for (const auto& course_and_prerequisite : prerequisites) {
            const int course = course_and_prerequisite[0];
            const int prerequisite = course_and_prerequisite[1];
            course_prerequisites[course].push_back(prerequisite);
        }

        std::set<int> taken;
        for (int course = 0; course < numCourses; ++course) {
            std::set<int> taking;
            if (HasCycle(course, course_prerequisites, taking, taken)) {
                return false;
            }
        }

        return true;
    }

private:
    bool HasCycle(int course,
                  const std::vector<std::vector<int>>& course_prerequisites,
                  std::set<int>& taking,
                  std::set<int>& taken) {
        if (taking.contains(course)) {
            return true;
        }
        if (taken.contains(course)) {
            return false;
        }

        taking.insert(course);
        for (const auto& prerequisite : course_prerequisites[course]) {
            if (HasCycle(prerequisite, course_prerequisites, taking, taken)) {
                return true;
            }
        }
        taking.erase(course);
        taken.insert(course);
        return false;
    }
};
