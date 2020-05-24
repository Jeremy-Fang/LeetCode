class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        A = sorted(A)
        B = sorted(B)
        M = len(A)
        N = len(B)
        i = j = 0
        res = []
        
        if not M or not N:
            return []
        
        while i < M and j < N:
            low = max(A[i][0], B[j][0])
            high = min(A[i][1],B[j][1])
            
            if low <= high:
                res.append([low, high])
            
            if high == A[i][1]:
                i += 1
            else:
                j += 1
                
        return res
