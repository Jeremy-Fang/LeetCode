class Solution:
    
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = collections.defaultdict(list)
        
        for u, v, w in edges:
            d[u].append((v,w))
            d[v].append((u,w))
            
        m = [[float("inf") for i in range(n)] for i in range(n)]
        c = {}
        
        for i in range(n):
            m[i][i] = 0
            
        for i in d.keys():
            for j in d[i]:
                m[i][j[0]] = j[1]
                
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if m[j][k] > m[j][i] + m[i][k]:
                        m[j][k] = m[j][i] + m[i][k]
                        
        for i in range(n):
            c[i] = 0
            for j in range(n):
                if m[i][j] <= distanceThreshold and i != j:
                    c[i] += 1
                    
        mi = min(c.values())
        ci = list(filter(lambda i: c[i] == mi, c.keys()))
        
        return max(ci)
