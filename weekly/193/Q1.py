class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ps = [0] * len(nums)
        
        for i, num in enumerate(nums):
            ps[i] = ps[i-1] + num
            
        return ps
