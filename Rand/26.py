class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 1
        
        while r < len(nums):
            if nums[r] == nums[r-1]:
                nums.pop(r)
            else:
                r += 1
