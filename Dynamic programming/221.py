class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M = len(matrix)
        ma = 0
        
        if not M:
            return 0
        
        N = len(matrix[0])
        
        dp = [[0 for i in range(N + 1)] for _ in range(M + 1)]
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    ma = max(ma, dp[i+1][j+1])
                    
        return ma ** 2
