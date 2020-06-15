class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        delta = collections.Counter(nums)
        unique = set(nums)
        res = []
        
        def backtrack(curr):
            nonlocal delta, unique, res
            
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            else:
                for num in unique:
                    if delta[num] > 0:
                        delta[num] -= 1
                        curr.append(num)
                        backtrack(curr)
                        curr.pop()
                        delta[num] += 1
                        
        backtrack([])
        
        return res
