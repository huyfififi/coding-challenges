class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_to_dependencies = {course: set() for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            course_to_dependencies[course].add(prerequisite)

        def exclude_course(excluding_course: int) -> None:
            course_to_dependencies.pop(excluding_course)
            for course in course_to_dependencies.keys():
                course_to_dependencies[course] -= {excluding_course}

        while course_to_dependencies:
            courses_without_dependencies = [
                course
                for course, dependencies in course_to_dependencies.items()
                if not dependencies
            ]
            if not courses_without_dependencies:
                return False

            for course in courses_without_dependencies:
                exclude_course(course)

        return True
