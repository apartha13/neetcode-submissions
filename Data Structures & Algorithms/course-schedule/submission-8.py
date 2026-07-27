class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {course: [] for course in range(numCourses)}

        for course, pre in prerequisites:
            courses[course].append(pre)
        
        for course in range(numCourses):
            stack = [(course, set())]
            while stack:
                curr, visited = stack.pop()
                if curr in visited:
                    return False
                visited.add(curr)
                for pre in courses[curr]:
                    stack.append((pre, visited.copy()))
        
        return True
