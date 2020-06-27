class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        offset = 0
        N = len(nums)
        
        if not N:
            return False
        
        for i in range(N):
            if nums[i-1] > nums[i]:
                offset = i
               
        low = 0
        high = (N - 1)
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[(mid+offset)%N] == target:
                return True
            elif nums[(mid+offset)%N] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
