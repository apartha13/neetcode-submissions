class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {course: [] for course in range(numCourses)}

        for course, pre in prerequisites:
            courses[course].append(pre)
        
        for course in range(numCourses):
            stack = [(course, set())]
            while stack:
                cur_course, visited = stack.pop()
                if cur_course in visited:
                    return False
                visited.add(cur_course)
                for pre in courses[cur_course]:
                    stack.append((pre, visited.copy()))
            courses[course] = []
        return True
