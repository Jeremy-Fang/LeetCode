class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        Y = len(board)
        X = len(board[0])
        adj = {(-1,0),(0,-1),(1,0),(0,1)}
        
        def go(prev, y, x, i):
            nonlocal l, Y, X, adj, board, word
            
            if board[y][x] == word[i]:
                c = board[y][x]
                board[y][x] = "."
                prev += c
                i += 1
                
                if len(prev) == l:
                    return True
                
                for dy, dx in adj:
                    if -1 < (y+dy) < Y and -1 < (x+dx) < X:
                        if go(prev, (y+dy), (x+dx), i):
                            return True
                    
                board[y][x] = c
                    
            return False
        
        for i in range(Y):
            for j in range(X):
                if go("", i, j, 0):
                    return True
                
        return False
