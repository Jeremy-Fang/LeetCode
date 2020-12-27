class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        sum = 0
        mx = 0
        start = 0
        N = len(nums)
        
        
        for i in range(N):
            if nums[i] in s:
                while sum > 0 and nums[i] in s:
                    s.remove(nums[start])
                    sum -= nums[start]
                    start += 1
                    
            s.add(nums[i])
            sum += nums[i]
            mx = max(mx, sum)
        
        return mx
