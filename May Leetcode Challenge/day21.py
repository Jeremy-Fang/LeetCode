class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0 for j in range(N+1)] for i in range(M+1)]
        res = 0
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j]:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    res += dp[i+1][j+1]
        
        return res
