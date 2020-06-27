class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        N = len(nums)
        
        def backtrack(curr, max_index):
            nonlocal res, nums, N
            res.append(curr.copy())
            
            for i in range(max_index + 1, N):
                curr.append(nums[i])
                backtrack(curr, i)
                curr.pop()
                
        backtrack([], -1)
        
        return res
