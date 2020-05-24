class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l = r = 0
        b = 0
        ma = 0
        L = len(A)
        
        while r < L:
            b += (A[r] == 0)
            
            while l < r and b > K:
                b -= (A[l] == 0)
                l += 1
            
            if b == K:
                ma = max(ma, r - l + 1)
            
            r += 1
        
        if (b < K):
            return max(ma, r - l)
        return ma
