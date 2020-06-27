class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        
        if not rows:
            return 0
        
        cols = len(grid[0])
        
        if not cols:
            return 0
        
        count = 0
        states = [[0] * cols for _ in range(rows)]
        adj = {(-1,0),(1,0),(0,-1),(0,1)}
        
        def dfs(x, y, pending):
            nonlocal adj, grid, rows, cols
            
            pending.append((x,y))
            
            for dx, dy in adj:
                nextX, nextY = x+dx, y+dy
                
                if 0 <= nextX < rows and 0 <= nextY < cols:
                    if grid[nextX][nextY] == "1" and states[nextX][nextY] == 0:
                        states[nextX][nextY] = 1
                        dfs(nextX, nextY, pending)
                        
                    
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1" and states[x][y] == 0:
                    pending = []
                    dfs(x, y, pending)
                    count += 1
                    
                    for pendX, pendY in pending:
                        states[pendX][pendY] = 2
        
        return count
