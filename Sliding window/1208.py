class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        L = len(s)
        l = r = 0
        ma = 0
        sum = 0
        
        while r < L:
            sum += cost[r]
            r += 1
            
            while l < r and sum > maxCost:
                sum -= cost[l]
                l += 1
                
            if sum <= maxCost:
                    ma = max(ma, r - l)
            
        return ma
            
