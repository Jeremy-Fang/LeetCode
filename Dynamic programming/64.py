class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        
        for i in range(M):
            for j in range(N):
                if i == 0:
                    if j == 0:
                        grid[i][j] = grid[i][j] 
                    else:
                        grid[i][j] += grid[i][j-1]
                else:
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                        
        return grid[-1][-1]
