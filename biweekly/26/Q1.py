class Solution:
    def maxPower(self, s: str) -> int:
        l = r = 0
        N = len(s)
        ma = 0
        
        while r < N:
            if s[l] != s[r]:
                l = r
            else:
                ma = max(ma, r - l + 1)
            r += 1
            
        return ma
