class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M = len(word1)
        N = len(word2)
        prev = None
        curr = [0] * (N+1)
        
        for i in range(M+1):
            for j in range(N+1):
                if i == 0:
                    curr[j] = j
                elif j == 0:
                    curr[0] = i
                elif word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
            prev = curr
            curr = [0] * (N+1)
                    
        return prev[-1]
