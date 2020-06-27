class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        N = len(nums)
        
        nums.sort()
            
        def backtrack(curr, mx):
            nonlocal res, N, nums
            
            res.append(curr.copy())
            
            for i in range(mx + 1, N):
                if i <= mx + 1 or nums[i] != nums[i-1]:
                    curr.append(nums[i])
                    backtrack(curr, i)
                    curr.pop()
                    
            
        backtrack([], -1)
        
        return res
