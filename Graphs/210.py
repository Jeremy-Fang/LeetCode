class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []
        preq = collections.defaultdict(list)
        process = [-1] * numCourses
        
        for course, prereq in prerequisites:
            preq[course].append(prereq)
            
        def dfs(course):
            nonlocal preq
            
            if process[course] == 1:
                return True
            
            if process[course] == 0:
                return False
            
            process[course] = 0
            
            for p in preq[course]:
                if not dfs(p):
                    return False
                
            process[course] = 1
            stack.append(course)
            
            return True
        
        for course in range(numCourses):
            if process[course] != -1:
                continue
            if process[course] == -1:
                if not dfs(course):
                    return []
            
        return stack
