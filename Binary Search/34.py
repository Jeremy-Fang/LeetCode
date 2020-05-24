class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(a, target):
            l = 0
            r = len(a)-1
            
            while l <= r:
                m = (l + r) // 2
                
                if a[m] > target:
                    r = m - 1
                elif a[m] < target:
                    l = m + 1
                else:
                    return m
                
            return -1
        
        l = r = binarySearch(nums, target)
        
        
        if l == -1:
            return [-1, -1]
        
        while l > 0 and nums[l-1] == target:
            l -= 1
            
        while r < len(nums)-1 and nums[r+1] == target:
            r += 1
            
        return [l, r]
