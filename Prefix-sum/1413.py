class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ps = 0
        mi = 0
        
        for num in nums:
            ps += num
            mi = min(mi, ps)
            
        return abs(mi) + 1
