#include <queue>
#include <vector>

class Solution {
public:
    bool canFinish(int numCourses, const std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> prerequisite_to_dependents(numCourses);
        std::vector<int> remaining_prerequisites_count(numCourses, 0);
        for (const auto& course_and_prerequisite : prerequisites) {
            const int course = course_and_prerequisite[0];
            const int prerequisite = course_and_prerequisite[1];
            prerequisite_to_dependents[prerequisite].push_back(course);
            ++remaining_prerequisites_count[course];
        }

        std::queue<int> takable_courses;
        for (int course = 0; course < numCourses; ++course) {
            if (remaining_prerequisites_count[course] == 0) {
                takable_courses.push(course);
            }
        }

        while (!takable_courses.empty()) {
            const int course = takable_courses.front();
            takable_courses.pop();
            for (const auto& dependent : prerequisite_to_dependents[course]) {
                --remaining_prerequisites_count[dependent];
                if (remaining_prerequisites_count[dependent] == 0) {
                    takable_courses.push(dependent);
                }
            }
        }

        for (const auto& count : remaining_prerequisites_count) {
            if (count > 0) {
                return false;
            }
        }
        return true;
    }
};
