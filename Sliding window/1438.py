class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = r = 0
        L = len(nums)
        longest = 0
        ma = 0
        mi = float('inf')
        
        
        while r < L:
            ma = max(ma, nums[r])
            mi = min(mi, nums[r])
            r += 1
            
            if ma - mi > limit:
                while nums[l] != mi and nums[l] != ma:
                    l += 1
                    
                if nums[l] == mi:
                    mi = min(nums[l+1:r])
                else:
                    ma = max(nums[l+1:r])
                        
                l += 1
            else:
                longest = max(longest, r - l)
            
        return longest
