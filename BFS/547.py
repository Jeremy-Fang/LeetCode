class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        q = []
        seen = set()
        edges = collections.defaultdict(list)
        groups = 0
        
        for i in range(N):
            for j in range(N):
                if i != j and M[i][j]:
                    edges[i].append(j)
        
        for i in range(N):
            if i not in seen:    
                q.append(i)
                while q:
                    for person in q:
                        p = q.pop(0)
                        
                        for neighbor in edges[p]:
                            if neighbor not in seen:
                                q.append(neighbor)
                                seen.add(neighbor)
                groups += 1
            seen.add(i)
            
        return groups
