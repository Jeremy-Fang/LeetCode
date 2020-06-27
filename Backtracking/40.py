class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        N = len(candidates)
        
        def backtrack(curr, max_index, target):
            nonlocal res
            if target == 0:
                res.append(curr.copy())
                return
            
            for i in range(max_index + 1, N):
                if i > max_index + 1 and candidates[i] == candidates[i-1]:
                    continue
                if target - candidates[i] >= 0:
                    curr.append(candidates[i])
                    backtrack(curr, i, target - candidates[i])
                    curr.pop()
                
        
        backtrack([], -1, target)
        
        return res
