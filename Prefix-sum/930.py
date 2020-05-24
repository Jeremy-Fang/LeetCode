class Solution:
    def numSubarraysWithSum(self, A, S):
        sum = res = 0
        d = collections.defaultdict(int)
        d[0] = 1
        
        for a in A:
            sum += a
            
            if sum-S in d:
                res += d[sum-S]
            d[sum] += 1
            
        return res

