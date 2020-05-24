class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        ps = [0] * N
        ps[0] = cost[0]
        ps[1] = cost[1]
        
        for i in range(2, N):
            ps[i] = min(ps[i-1], ps[i-2]) + cost[i]
            
        return min(ps[-1], ps[-2])
