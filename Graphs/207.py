class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        unlocks = collections.defaultdict(list)
        process = [-1] * numCourses
        
        for course, prereq in prerequisites:
            unlocks[prereq].append(course)
            
        def dfs(course):
            nonlocal unlocks, process
            if process[course] == 0:
                return False
            
            if process[course] == 1:
                return True
            
            process[course] = 0
            
            for unlocked in unlocks[course]:
                if not dfs(unlocked):
                    return False
                
            process[course] = 1
            return True
        
        for course in range(numCourses):
            if process[course] != -1:
                continue
                
            if not dfs(course):
                return False
            
        return True
    
    
            
