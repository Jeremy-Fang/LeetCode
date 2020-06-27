class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = 0
        zeros = 0
        N = len(nums)
        start = 0
        
        for end in range(N):
            if nums[end] == 0:
                zeros += 1
                
                while start < end and zeros > 1:
                    if nums[start] == 0:
                        zeros -= 1
                    start += 1
                    
            mx = max(mx, end - start)
            
        return mx
