class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        for i in range(len(difficulty)):
            difficulty[i] = (difficulty[i], profit[i])
        
        difficulty = sorted(difficulty, key= lambda i: i[0])
        res = 0
        l = 0
        ma = 0
        
        for i in sorted(worker):
            while l < len(difficulty) and i >= difficulty[l][0]:
                ma = max(ma, difficulty[l][1])
                l += 1
            res += ma
            
        return res
