#include <vector>

class Solution {
public:
    bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
        std::vector<std::vector<int>> course_to_prerequisites(numCourses);
        for (const auto& course_and_prerequisite : prerequisites) {
            int course = course_and_prerequisite[0];
            int prerequisite = course_and_prerequisite[1];
            course_to_prerequisites[course].push_back(prerequisite);
        }

        std::vector<VisitState> visit_states(numCourses, VisitState::kNotYetVisited);
        for (int course = 0; course < numCourses; ++course) {
            if (Traverse(course, course_to_prerequisites, visit_states)) {
                return false;
            }
        }
        return true;
    }

private:
    enum class VisitState {
        kNotYetVisited,
        kVisiting,
        kVisited,
    };
    // Returns true if a cycle is detected starting from this course.
    // Returns false otherwise.
    bool Traverse(int course,
                  const std::vector<std::vector<int>>& course_to_prerequisites,
                  std::vector<VisitState>& visit_states) {
        if (visit_states[course] == VisitState::kVisiting) {
            return true;
        }
        if (visit_states[course] == VisitState::kVisited) {
            return false;
        }

        visit_states[course] = VisitState::kVisiting;
        for (const auto& prerequisite : course_to_prerequisites[course]) {
            if (Traverse(prerequisite, course_to_prerequisites, visit_states)) {
                return true;
            }
        }
        visit_states[course] = VisitState::kVisited;
        return false;
    }
};
