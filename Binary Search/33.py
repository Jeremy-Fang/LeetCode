class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = None
        N = len(nums)
        
        if not N:
            return -1
        
        for i in range(N):
            if nums[i-1] > nums[i]:
                offset = i
               
        low = 0
        high = (N - 1)
        
        if offset == None:
            if nums[low] == target:
                return low
            else:
                return -1
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[(mid+offset)%N] > target:
                high = mid - 1
            elif nums[(mid+offset)%N] < target:
                low = mid + 1
            else:
                return (mid + offset)%N
            
        return -1
