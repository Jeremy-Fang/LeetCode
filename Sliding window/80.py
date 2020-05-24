class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        
        
        while r < len(nums):
            while r < len(nums) and nums[r] == nums[r-1]:
                r += 1
            
            while r - l > 2:
                nums.pop(l)
                r -= 1
                
            l = r
            r += 1
            
        return len(nums)
