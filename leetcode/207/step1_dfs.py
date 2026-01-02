class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_to_prerequisites = {course: set() for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            course_to_prerequisites[course].add(prerequisite)

        visited = set()

        def visit(course: int, visiting: set[int]) -> bool:
            if course in visited:
                return False
            if course in visiting:
                return True

            visiting.add(course)
            for prerequisite in course_to_prerequisites[course]:
                if visit(prerequisite, visiting):
                    return True

            visited.add(course)
            return False

        for course in range(numCourses):
            if visit(course, set()):
                return False

        return True
