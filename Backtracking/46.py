class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(curr):
            nonlocal res
            nonlocal nums
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            else:
                for num in nums:
                    if num not in curr:
                        curr.append(num)
                        backtrack(curr)
                        curr.pop()
                    
        backtrack([])
        
        return res
