class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sum = res = 0
        d = collections.defaultdict(int)
        d[0] = 1
        
        for num in nums:
            if num % 2 == 1:
                sum += 1
            
            if sum-k in d:
                res += d[sum-k]
            d[sum] += 1
            
        return res
