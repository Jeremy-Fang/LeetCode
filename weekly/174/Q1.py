class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = [(i, mat[i].count(1)) for i in range(len(mat))]
        m = sorted(m, key=lambda i: i[1])
        
        return [m[i][0] for i in range(k)]
