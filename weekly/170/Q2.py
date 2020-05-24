class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        M = len(queries)
        dp = [0] * N
        dp[0] = arr[0]
        res = []
        
        for i in range(1, N):
            dp[i] = dp[i-1] ^ arr[i]
            
        for i in range(M):
            if queries[i][0] == queries[i][1]:
                res.append(arr[queries[i][0]])
            else:
                if queries[i][0] != 0:
                    res.append(dp[queries[i][1]] ^ dp[queries[i][0]-1])
                else:
                    res.append(dp[queries[i][1]])
        
        return res
