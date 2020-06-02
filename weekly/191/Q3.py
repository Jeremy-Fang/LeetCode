class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        path = set([0])
        count = 0
        
        for start, end in connections:
            if start in path and end not in path:
                path.add(end)
                count += 1
            elif end in path and start not in path:
                path.add(start)
                    
        return count 
