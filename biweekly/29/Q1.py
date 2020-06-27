class Solution:
    def average(self, salary: List[int]) -> float:
        mn, mx = float('inf'), float('-inf')
        N = len(salary)
        
        if N <= 2:
            return 0
        
        for s in salary:
            mn = min(mn, s)
            mx = max(mx, s)
            
        return (sum(salary) - mn - mx) / (N-2)
