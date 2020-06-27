class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(curr, mx):
            nonlocal n, k, res
            
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(mx + 1, n + 1):
                curr.append(i)
                backtrack(curr, i)
                curr.pop()
                
        backtrack([], 0)
        
        return res
