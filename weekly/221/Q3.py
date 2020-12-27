class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M = len(grid)
        N = len(grid[0])
        res = [-1] * N
        
        def trav(i, j, top):
            nonlocal M, N, grid
            if i == M:
                return j
            if top:
                if j == 0 and grid[i][j] == -1:
                    return -1
                if j == N - 1 and grid[i][j] == 1:
                    return -1
                if grid[i][j] == 1 and grid[i][j+1] == -1:
                    return -1
                if grid[i][j] == -1 and grid[i][j-1] == 1:
                    return -1
                if grid[i][j] == 1:
                    return trav(i,j+1,not top)
                else:
                    return trav(i,j-1,not top)
            else:
                return trav(i+1,j,not top)
            
                
        
        for i in range(N):
            res[i] = trav(0, i, True)
            
        return res
