class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        odds = [-1] + [i for i in range(len(nums)) if nums[i] % 2 == 1] + [len(nums)]
        
        for i in range(1, len(odds)-k):
            l = odds[i] - odds[i-1] - 1
            r = odds[i+k] - odds[i+k-1] - 1
            res += (l+1) * (r+1)
        
        return res
