class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        for i in range(len(difficulty)):
            difficulty[i] = (difficulty[i], profit[i])
        
        difficulty = sorted(difficulty, key= lambda i: i[0])
        
        i = 1
        
        while i < len(difficulty):
            if difficulty[i][0] == difficulty[i-1][0]:
                if difficulty[i][1] > difficulty[i-1][1]:
                    difficulty.remove(difficulty[i-1])
                else:
                    difficulty.remove(difficulty[i])
            else:
                i += 1
                
        ps = [0] * (len(difficulty) + 1)
        
                    
        for i in range(1, len(ps)):
            ps[i] = max(ps[i-1], difficulty[i-1][1])
        
        l = 0
        res = 0
        
        for i in sorted(worker):
            while l < len(ps) - 1 and i > difficulty[l][0]:
                l += 1
            
            if l == len(ps) - 1:
                res += ps[-1]
            else:
                if i == difficulty[l][0]:
                    res += ps[l+1]
                else:
                    res += ps[l]
        
        return res
