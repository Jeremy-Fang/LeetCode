class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        dp = [0] * N
        mx = 0
        
        if N == 0 or N == 1:
            return 0
        
        if s[0] == '(' and s[1] == ')':
            dp[1] = mx = 2
        
        for i in range(2, N):
            if s[i-1] == '(' and s[i] == ')':
                dp[i] = dp[i-2] + 2
                mx = max(mx, dp[i])
            else:
                if s[i-1] == ')' and s[i] == ')':
                    if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                        mx = max(mx, dp[i])
        
        return mx
