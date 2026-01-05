#include <map>
#include <set>
#include <vector>

class Solution {
public:
    bool canFinish(int numCourses, const std::vector<std::vector<int>>& prerequisites) {
        std::map<int, std::set<int>> course_to_prerequisites;
        for (int course = 0; course < numCourses; ++course) {
            course_to_prerequisites.emplace(course, std::set<int>{});
        }
        for (const auto& course_and_prerequisite : prerequisites) {
            int course = course_and_prerequisite[0];
            int prerequisite = course_and_prerequisite[1];
            course_to_prerequisites[course].insert(prerequisite);
        }

        std::vector<int> takable_courses = FilterTakableCourses(course_to_prerequisites);
        while (takable_courses.size() > 0) {
            for (const auto& course : takable_courses) {
                TakeCourse(course, course_to_prerequisites);
            }
            takable_courses = FilterTakableCourses(course_to_prerequisites);
        }

        return course_to_prerequisites.size() == 0;
    }

private:
    std::vector<int> FilterTakableCourses(const std::map<int, std::set<int>>& course_to_prerequisites) {
        std::vector<int> takable_courses;
        for (const auto& [course, prerequisites] : course_to_prerequisites) {
            if (prerequisites.size() == 0) {
                takable_courses.push_back(course);
            }
        }
        return takable_courses;
    }
    void TakeCourse(int course_to_take, std::map<int, std::set<int>>& course_to_prerequisites) {
        course_to_prerequisites.erase(course_to_take);
        for (auto& [_, prerequisites] : course_to_prerequisites) {
            prerequisites.erase(course_to_take);
        }
    }
};
