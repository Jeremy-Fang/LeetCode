class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        d = collections.defaultdict(list)
        v = collections.defaultdict(list)
        N = len(friends)
        
        for i in range(N):
            for j in friends[i]:
                d[i].append(j)
            for j in watchedVideos[i]:
                v[i].append(j)
                
        m = [[float("inf") for i in range(N)] for j in range(N)]
        
        for i in range(N):
            m[i][i] = 0
            
        for i in d.keys():
            for j in d[i]:
                m[i][j] = 1
                
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if m[j][k] > m[j][i] + m[i][k]:
                        m[j][k] = m[j][i] + m[i][k]
        
        f = []
        vres = {}
        
        for i in range(N):
            if m[id][i] == level:
                f.append(i)
                
        for i in f:
            for j in v[i]:
                if j not in vres:
                    vres[j] = 1
                else:
                    vres[j] += 1
                    
        res = sorted([(i, vres[i]) for i in sorted(vres.keys())], key=lambda i: i[1])
        
        return [i for i, j in res]
                        
        
