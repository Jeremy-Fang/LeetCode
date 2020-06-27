class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        rows = len(image)
        
        if not rows:
            return image
        
        cols = len(image[0])
        
        if not cols:
            return image
        
        seen = [[0] * cols for _ in range(rows)]
        adj = {(-1,0),(1,0),(0,-1),(0,1)}
        
        def dfs(x, y, pending):
            nonlocal rows, cols, adj, seen
            pending.append((x,y))
            
            for dx, dy, in adj:
                nextX, nextY = x+dx, y+dy
                
                if 0 <= nextX < rows and 0 <= nextY < cols:
                    if not seen[nextX][nextY] and image[x][y] == image[nextX][nextY]:
                        seen[nextX][nextY] = 1
                        dfs(nextX, nextY, pending)
                        
        pending = []
        seen[sr][sc] = 1
        dfs(sr, sc, pending)
        
        for pendX, pendY in pending:
            image[pendX][pendY] = newColor
            
        return image
