class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        l = r = 0 
        L = len(A)
        ma = 2
        
        # if r odd, r+1 must be smaller and 
        # if r even, r+1 must be greater
        # OR
        # if r odd, r+1 must be greater and
        # if r even, r+1 must be smaller
        
        if A.count(A[0]) == L:
            return 1
        
        while r < L - 2:
            if (A[r] > A[r+1] and A[r+1] < A[r+2]) or (A[r] < A[r+1] and A[r+1] > A[r+2]):
                ma = max(ma, r - l + 3)
            else:
                l = r + 1
            r += 1
            
        return ma
