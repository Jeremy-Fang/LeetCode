class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        unlocks = collections.defaultdict(list)
        numOfPre = [0] * (n + 1)
        
        for prereq, course in dependencies:
            unlocks[prereq].append(course)
            numOfPre[course] += 1
            
        heap = []
        count = 0
        
        for i in range(1, n + 1):
            if numOfPre[i] == 0:
                heapq.heappush(heap, (-len(unlocks[i]), i))
        
        while heap:
            added = []
            
            for i in range(k):
                if not heap:
                    break
                _, course = heapq.heappop(heap)
                for unlocked in unlocks[course]:
                    numOfPre[unlocked] -= 1
                    if numOfPre[unlocked] == 0:
                        heapq.heappush(added, (-len(unlocks[unlocked]), unlocked))
            
            count += 1
            for item in added:
                heapq.heappush(heap, item)
            
        return count
