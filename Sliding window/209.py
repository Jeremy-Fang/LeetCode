class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = r = 0
        L = len(nums)
        mi = float('inf')
        sum = 0
        
        while r < L:
            sum += nums[r]
            r += 1
            
            while sum >= s:
                sum -= nums[l]
                mi = min(mi, r - l)
                l += 1
            
        if mi == float('inf'):
            return 0
        return mi
